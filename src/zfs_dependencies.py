#!/usr/bin/env python3
'''Get antlet dependencies'''

from subprocess import Popen, PIPE
import argparse
from pprint import pprint as pp
from sample_data import *


def _get_zfs_name_origin_list():
    '''Gets a list of strings, each containing the zfs name and origin - incluedes snapshots'''

    zfs_list = []

    # get zfs list with snapshots and origins
    with Popen(["zfs list -H -t filesystem,snapshot -o name,origin | grep -v antlets/_docker"],
                shell=True, stdout=PIPE) as lister:

        for bytes in lister.stdout:
            line = bytes.decode().strip()
            zfs_list.append(line)

    return zfs_list


def create_dependency_list(zlist):
    '''Creates a dependency list from the 'name origin' list. 
    It is a list of dict's, one for each zfs name. 
    Keys are:
        'name':  String - zfs name
        'parent' String - parent zfs name
        'children' List of Strings - zfs names of dependent children'''

    # convert each name,origin string into a dict
    for index, item in enumerate(zlist):
        name, _, origin = item.partition('\t')
        zlist[index] = {'name':name, 'parent': origin}

    # populate empty 'parent' values
    for item in zlist:
        if item['parent'] != '-':
            continue
        elif '@' in item['name']:
            parent_name = item['name'].partition('@')[0]
            item['parent'] = parent_name
        else:
            item['parent'] = None

    # populate 'children' values
    '''Does the current zfs name == another item 'parent' name'''
    for parent_item in zlist:
        children = []
        for item in zlist:
            if parent_item['name'] == item['parent']:
                children.append(item['name'])
        parent_item = parent_item.update({'children': children})

    return zlist




def insert_children(zobj):
    for item in dependency_list:
        if zobj['name'] == item['name']:
            for child in item['children']:
                new_zobj = {'name': child, 'children': []}
                zobj['children'].append(new_zobj)
                insert_children(new_zobj)


def create_json_list(dependency_list):
    jlist = []
    # Create list of top level zfs (zfs with no parents)
    for item in dependency_list:
        if not item['parent']:
            jlist.append({'name': item['name'], 'children': []})

    # add chidren recursively
    for jitem in jlist:
        insert_children(jitem)

    return jlist







def _get_zfs_item(zfs_name):

    for item in dependency_list:
        if item['name'] == zfs_name:
            return item


def _get_parent_list(zfs_name):
    parent_list = []

    parent = _get_zfs_item(zfs_name)['parent']
    count = 0 # protect against infinit loop

    while parent != None and count < 20:
        parent_list.append(parent)
        parent = _get_zfs_item(parent)['parent']
        count += 1

    parent_list.reverse()
    return parent_list


def show_parents(zfs_name):
    parent_list = _get_parent_list(zfs_name)
    parent_list.append(zfs_name)
    indent = " " * 4
    next_level = "\u2514\u2500\u2500 "
    count = -1
    for item in parent_list:
        if count < 0:
            prefix = ""
        else:
            prefix = "{}{}".format(indent * count, next_level)

        print(prefix + item)
        count += 1


def show_children(zfs_name):
    global dependency_list
    print(zfs_name)

    def _show_child_tree(zfs_name, depth=0):
        indent = " " * 3
        next_level = "\u2514\u2500 "
        for item in dependency_list:
            if zfs_name == item['name']:
                for i in item['children']:
                    prefix = "{}{}".format((indent * (depth-1)), next_level)
                    print("{}{}".format(prefix, i))
                    _show_child_tree(i, depth+1)

    _show_child_tree(zfs_name, 1)


def show_tree(zfs=None):
    if zfs:
        # show tree for specific zfs
        show_parents(zfs)
        show_children(zfs)
    #else:
        # show entire tree.. all trees


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('zfs_name', help='the zfs name as seen with `zfs list -o name`')
    parser.add_argument('-t', help="use sample data", choices=range(0,25), type=int)
    args = parser.parse_args()

    global dependency_list
    global json_list

    if args.t == 0:
        _zfs_name_origin_list = nolist0()
    elif args.t == 1:
        _zfs_name_origin_list = nolist1()
    elif args.t == 2:
        _zfs_name_origin_list = nolist2()
    elif args.t == 11:
        _zfs_name_origin_list = nolist11()
    elif args.t == 12:
        _zfs_name_origin_list = nolist12()
    elif args.t == 24:
        _zfs_name_origin_list = nolist24()
    else:
        _zfs_name_origin_list = _get_zfs_name_origin_list()

    #pp(_zfs_name_origin_list) 

    dependency_list = create_dependency_list(_zfs_name_origin_list)
    #pp(dependency_list)

    json_list = create_json_list(dependency_list)
    print("** json list:")
    pp(json_list)
    print()

    #show_children(args.zfs_name)



if __name__ == '__main__':
    main()
