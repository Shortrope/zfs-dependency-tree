#!/usr/bin/python3

from subprocess import Popen, PIPE
import re
from pprint import pprint as pp


# Create zfs list with snapshots
def get_zfs_list(zlist=None):

    
    if not zlist:
        zlist = []
        # get zfs list with snapshots and origins
        with Popen(["zfs list -H -t filesystem,snapshot -o name,origin | grep -v antlets/_docker"],
                    shell=True, stdout=PIPE) as lister:

            for bytes in lister.stdout:
                line = bytes.decode().strip()
                zlist.append(line)

    # convert each name,origin string into a map
    for index, item in enumerate(zlist):
        name, _, origin = item.partition('\t')
        zlist[index] = {'name':name, 'parent': origin}

    # populate 'parent' value for each zfs item
    for item in zlist:
        if item['parent'] != '-':
            continue
        elif '@' in item['name']:
            zfs = item['name'].partition('@')[0]
            item['parent'] = zfs
        else:
            item['parent'] = None

    return zlist



def add_children(zlist_w_parents):

    for item in zlist_w_parents:
        children = []
        index_of_parent = zlist_w_parents.index(item)
        for child_item in zlist_w_parents:
            if child_item.__contains__('parent_index') and child_item['parent_index'] == index_of_parent:
                child_index = zlist_w_parents.index(child_item)
                children.append(child_index)

        item.update({'children': children})
        new_zlist.append(item)


    return zlist_w_parents


def show_dependency_tree(zfs, zlist):
    pass

def main():

    zfs_list = get_zfs_list()
    #zfs_list_w_parents = add_parents(zfs_list)
    #zfs_list_w_children = add_children(zfs_list_w_parents)
#
    #print("")
    #for i, v in enumerate(zfs_list_w_children):
        #print("{}: {}".format(i, v))

    pp(zfs_list)


if __name__ == '__main__':
    main()
