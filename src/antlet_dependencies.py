#!/usr/bin/python3

from subprocess import Popen, PIPE
import re
from pprint import pprint as pp

zfs_list = []

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
                    item = (item, zlist.index(parent))
                elif "@" in item:
                    parent = item.partition('@')[0]
                    item = (item, zlist.index(parent))
                else:
                    item = (item, None)
                new_zlist.append(item)
                
    return new_zlist


def add_children(zlist_w_parents):
    new_zlist = []

    for item in zlist_w_parents:
        children = []
        item_index = zlist_w_parents.index(item)
        for i in zlist_w_parents:
            if i[1] == item_index:
                child_index = zlist_w_parents.index(i)
                children.append(child_index)

        new_zlist.append((item[0], item[1], children))

    return new_zlist



def main():

    zfs_list = get_zfs_list()
    zfs_list_w_parents = add_parents(zfs_list)
    zfs_list_w_children = add_children(zfs_list_w_parents)
    #pp(zfs_list)
    pp(zfs_list_w_children)


if __name__ == '__main__':
    main()