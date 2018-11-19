from subprocess import Popen, PIPE
import re
from pprint import pprint as pp

zfs_list = []

# Create zfs list with snapshots
def get_zfs_list():

    zlist = []

    lister = Popen(["zfs list -H -t all -o name | grep -v antlets/_docker"], shell=True, stdout=PIPE)
    for bytes in lister.stdout:
        line = bytes.decode().strip()
        zlist.append(line)

    return zlist


def add_parents(zlist):
    new_zlist = []
    for item in zlist:

        lister = Popen("zfs list -H -o origin {}".format(item), shell=True, stdout=PIPE)
        for bytes in lister.stdout:
            parent = bytes.decode().strip()
            if parent in zlist:
                item = (item, zlist.index(parent))
            else:
                item = (item, None)
            new_zlist.append(item)
                
    return new_zlist


def add_children(zlist_w_parents):
    new_zlist = []

    return new_zlist


def main():

    zfs_list = get_zfs_list()
    zfs_list_w_parents = add_parents(zfs_list)
    pp(zfs_list)


if __name__ == '__main__':
    main()