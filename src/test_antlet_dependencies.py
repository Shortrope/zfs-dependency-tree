#!/usr/bin/python3

import unittest
from antlet_dependencies import *


class TestAntletDependencies(unittest.TestCase):

    def setUp(self):
        self.zfs_type_all_list = ["antlets",
                        "antlets/Bazinga",
                        "antlets/Ubu1",
                        "antlets/Ubu2",
                        "antlets/Ubu3",
                        "antlets/Win10-base",
                        "antlets/Win10-base2",
                        "antlets/Win10-iso",
                        "antlets/Win10-iso@sysprep",
                        "antlets/Win10s",
                        "antlets/Win10s@uptodate",
                        "antlets/WinAddVirt",
                        "antlets/_templates",
                        "antlets/_templates/Blank",
                        "antlets/_templates/Blank@snap",
                        "antlets/_templates/CentOS-7.1.lxc",
                        "antlets/_templates/CentOS-7.1.lxc@snap",
                        "antlets/_templates/Fedora.lxc",
                        "antlets/_templates/Fedora.lxc@snap",
                        "antlets/_templates/Ubuntu16.04",
                        "antlets/_templates/Ubuntu16.04@snap",
                        "antlets/_templates/W10-1803-iso.kvm",
                        "antlets/_templates/W10-1803-iso.kvm@1803",
                        "antlets/_templates/W10-1803-iso.kvm@snap",
                        "antlets/_templates/Win10",
                        "antlets/_templates/Win10@snap",
                        "antlets/_templates/Win10-1803-spc.kvm",
                        "antlets/_templates/Win10-1803-spc.kvm@1803",
                        "antlets/_templates/Win10-1803-spc.kvm@snap",
                        "antlets/_templates/Win10-Spice",
                        "antlets/_templates/Win10-Spice@snap",
                        "antlets/_templates/Win2016",
                        "antlets/_templates/Win2016@snap",
                        "antlets/_templates/ant2s1-template.lxc",
                        "antlets/_templates/ant2s1-template.lxc@snap",
                        "antlets/_templates/ubuntu-xenial",
                        "antlets/_templates/ubuntu-xenial@snap",
                        "antlets/_tmp",
                        "antlets/ant1",
                        "antlets/ant1@s1",
                        "antlets/ant2",
                        "antlets/ant2@ant2-s1",
                        "antlets/ant2@ant2-s2",
                        "antlets/ant3",
                        "antlets/from-ant1-snap",
                        "antlets/isos"]


    def test_get_zfs_list_returns_a_list(self):
        result = get_zfs_list()
        self.assertIsInstance(result, list)


    def test_get_zfs_list_returns_a_list_of_stings(self):
        result = get_zfs_list()
        #result = self.zfs_type_all_list
        for item in result:
            self.assertIsInstance(item, str)


    def test_add_parents_parent_index_is_populated(self):
        result = add_parents(self.zfs_type_all_list)
        self.assertEqual(result[1][1], 34)
        self.assertEqual(result[3][1], 20)
        self.assertEqual(result[4][1], 20)

        
    def test_add_parents_snapshots_have_a_parent_index(self):
        result = add_parents(self.zfs_type_all_list)
        for item in result:
            if "@" in item[0]:
                self.assertIsNotNone(item[1])
                self.assertIsInstance(item[1], int)

    def test_add_children_adds_a_list_of_children_to_each_item(self):
        wparents = add_parents(self.zfs_type_all_list)
        wchildren = add_children(wparents)
        #print(wchildren)
        for item in wchildren:
            self.assertIsInstance(item[2], list)


    def test_add_children_specific_list(self):
        wparents = add_parents(self.zfs_type_all_list)
        wchildren = add_children(wparents)
        self.assertEqual(wchildren[20][2], [2,3,4])

if __name__ == '__main__':
    unittest.main()
