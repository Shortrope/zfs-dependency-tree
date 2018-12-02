#!/usr/bin/python3

from subprocess import Popen, PIPE
from pprint import pprint as pp


def get_zfs_name_origin_list():

    zfs_list = []

    # get zfs list with snapshots and origins
    with Popen(["zfs list -H -t filesystem,snapshot -o name,origin | grep -v antlets/_docker"],
                shell=True, stdout=PIPE) as lister:

        for bytes in lister.stdout:
            line = bytes.decode().strip()
            zfs_list.append(line)

    return zfs_list


def create_dependency_list(zlist):

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


def main():

    zfs_name_origin_list = get_zfs_name_origin_list()
    dependency_list = create_dependency_list(zfs_name_origin_list)
    pp(dependency_list)


if __name__ == '__main__':
    main()
