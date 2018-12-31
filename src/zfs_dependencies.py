#!/usr/bin/env python3
'''Get antlet dependencies'''

from subprocess import Popen, PIPE
from argparse import ArgumentParser
from pprint import pprint as pp
from sample_data import *


dependency_list = []


def create_parser():
    parser = ArgumentParser(description='Returns a zfs dependency tree. If no arguments are given the tree is printed in an easily readable format.')
    parser.add_argument('-j', '--json',
        help='return a json string',
        action='store_true')
    parser.add_argument('--version',
        action='version',
        version='%(prog)s 0.1.0')
    parser.add_argument('-t', help="use sample data", choices=[0,1,2,11,24], type=int)

    return parser



def get_zfs_name_origin_list():
    '''Gets a list of strings, each containing the zfs name and origin - incluedes snapshots'''

    zfs_name_origin_list = []

    # get zfs list with snapshots and origins
    with Popen(["zfs list -H -t filesystem,snapshot -o name,origin | grep -v antlets/_docker"],
                shell=True, stdout=PIPE) as lister:

        for bytes in lister.stdout:
            line = bytes.decode().strip()
            zfs_name_origin_list.append(line)

    return zfs_name_origin_list


def create_dependency_list(zfs_name_origin_list):
    '''Creates a dependency list from the 'name origin' list. 
    This is a list of dict's, one for each zfs name. 
    Keys are:
        'name':    String - zfs name
        'parent'   String - parent zfs name
        'children' List of Strings - zfs names of dependent children'''

    dependency_list = []

    # convert each name,origin string into a dict
    for item in zfs_name_origin_list:
        name, _, origin = item.partition('\t')
        dependency_list.append({'name':name, 'parent': origin})

    # populate empty 'parent' values
    for item in dependency_list:
        if item['parent'] != '-':
            continue
        elif '@' in item['name']:
            parent_name = item['name'].partition('@')[0]
            item['parent'] = parent_name
        else:
            item['parent'] = None

    # populate 'children' values
    '''Does the current zfs name == another item 'parent' name'''
    for parent_item in dependency_list:
        children = []
        for item in dependency_list:
            if parent_item['name'] == item['parent']:
                children.append(item['name'])
        parent_item = parent_item.update({'children': children})

    return dependency_list



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



def get_zfs_item(zfs_name):

    for item in dependency_list:
        if item['name'] == zfs_name:
            return item


def get_parent_list(zfs_name):
    parent_list = []

    parent = get_zfs_item(zfs_name)['parent']
    count = 0 # protect against infinit loop

    while parent != None and count < 20:
        parent_list.append(parent)
        parent = get_zfs_item(parent)['parent']
        count += 1

    parent_list.reverse()
    return parent_list


def show_parents(zfs_name):
    parent_list = get_parent_list(zfs_name)
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

def get_top_level_parent_list(dependency_list):
    top_level_parent_list = []
    for item in dependency_list:
        if not item['parent']:
            top_level_parent_list.append(item['name'])
    return top_level_parent_list


#def show_tree():


def main():
    parser = create_parser()
    args = parser.parse_args()

    global dependency_list
    global json_list

    if args.t == 0:
        zfs_name_origin_list = nolist0()
    elif args.t == 1:
        zfs_name_origin_list = nolist1()
    elif args.t == 2:
        zfs_name_origin_list = nolist2()
    elif args.t == 11:
        zfs_name_origin_list = nolist11()
    elif args.t == 12:
        zfs_name_origin_list = nolist12()
    elif args.t == 24:
        zfs_name_origin_list = nolist24()
    else:
        zfs_name_origin_list = get_zfs_name_origin_list()

    #pp(zfs_name_origin_list) 

    dependency_list = create_dependency_list(zfs_name_origin_list)
    #pp(dependency_list)


    if args.json:
        json_list = create_json_list(dependency_list)
        print("** json list:")
        pp(json_list)
        print()
    else:
        for top_level_item in get_top_level_parent_list(dependency_list):
            show_children(top_level_item)
            print()




if __name__ == '__main__':
    main()
