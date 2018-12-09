#!/usr/bin/python3
'''View antlet dependencies'''

from subprocess import Popen, PIPE
from pprint import pprint as pp


def get_zfs_name_origin_list():
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


def get_zfs(zfs_name):

    for item in dependency_list:
        if item['name'] == zfs_name:
            return item


def get_parent_list(zfs_name):
    parent_list = []

    parent = get_zfs(zfs_name)['parent']
    count = 0 # protect against infinit loop

    while parent != None and count < 20:
        parent_list.append(parent)
        parent = get_zfs(parent)['parent']
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


def _get_child_tree(zfs_name, depth=0):
    for item in dependency_list:
        if zfs_name == item['name']:
            for i in item['children']:
                indent = " " * 4
                next_level = "\u2514\u2500\u2500 "
                prefix = "{}{}".format((indent * (depth-1)), next_level)
                print("{}{}".format(prefix, i))
                _get_child_tree(i, depth+1)


def show_children(zfs_name):
    global dependency_list
    print(zfs_name)
    _get_child_tree(zfs_name, 1)



def show_tree(zfs=None):
    if zfs:
        # show tree for specific zfs
        show_parents(zfs)
        show_children(zfs)
    #else:
        # show entire tree.. all trees


def main():

    zfs_name_origin_list = get_zfs_name_origin_list()

    global dependency_list
    dependency_list = create_dependency_list(zfs_name_origin_list)

    #pp(dependency_list)
    #show_tree('antlets/ant1')
    show_tree('antlets/_templates/Win10')
    #show_parents('antlets/ant1')
    #show_children('antlets/_templates/ubuntu-xenial')
    #show_children('antlets/_templates/ubuntu-xenial@snap')
    #print(get_parent('antlets/ant2'))
    #print(get_parent('antlets/Win10-iso'))
    #print(get_parent('antlets/_templates/Win10@snap'))


if __name__ == '__main__':
    main()
