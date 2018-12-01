#!/usr/bin/python3

from subprocess import Popen, PIPE
import re
from pprint import pprint as pp


# Create zfs list with snapshots
def get_zfs_list():

    zlist = []

    with Popen(["zfs list -H -t all -o name | grep -v antlets/_docker"], shell=True, stdout=PIPE) as lister:
        for bytes in lister.stdout:
            line = bytes.decode().strip()
            zlist.append(line)

    return zlist


def add_parents(zlist):
    new_zlist = []
    for item in zlist:
        with Popen("zfs list -H -o origin {}".format(item), shell=True, stdout=PIPE) as lister:
            for bytes in lister.stdout:
                parent = bytes.decode().strip()
                if parent in zlist:
                    item = dict(zfs=item, parent_index=zlist.index(parent))
                elif "@" in item:
                    parent = item.partition('@')[0]
                    item = dict(zfs=item, parent_index=zlist.index(parent))
                else:
                    item = dict(zfs=item, parent_index=None)

                new_zlist.append(item)
                
    return new_zlist


def add_children(zlist_w_parents):

    new_zlist = []

    for parent_item in zlist_w_parents:
        children = []
        index_of_parent = zlist_w_parents.index(parent_item)
        for child_item in zlist_w_parents:
            if child_item.__contains__('parent_index') and child_item['parent_index'] == index_of_parent:
                child_index = zlist_w_parents.index(child_item)
                children.append(child_index)

        parent_item.update({'children': children})
        new_zlist.append(parent_item)


    return new_zlist


def show_dependency_tree(zfs, zlist):
    pass

def main():

    zfs_list = get_zfs_list()
    zfs_list_w_parents = add_parents(zfs_list)
    zfs_list_w_children = add_children(zfs_list_w_parents)

    print("")
    for i, v in enumerate(zfs_list_w_children):
        print("{}: {}".format(i, v))


if __name__ == '__main__':
    main()
