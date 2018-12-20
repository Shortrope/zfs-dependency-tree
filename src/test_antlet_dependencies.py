#!/usr/bin/python3


import unittest
from zfs_dependencies import *


class TestAntletDependencies(unittest.TestCase):

    def setUp(self):

        self.short_zfs_list = ["antlets\t-",
                        "antlets/_templates/ubuntu-xenial\t-",
                        "antlets/_templates/ubuntu-xenial@snap\t-",
                        "antlets/ant1\tantlets/_templates/ubuntu-xenial@snap",
                        "antlets/ant2\tantlets/_templates/ubuntu-xenial@snap",
                        "antlets/ant3\tantlets/_templates/ubuntu-xenial@snap"]

        self.short_dependency_list = [{
                                       'name': 'antlets',
                                       'children': [],
                                       'parent': None
                                      },
                                      {
                                       'name': 'antlets/_templates/ubuntu-xenial',
                                       'children': ['antlets/_templates/ubuntu-xenial@snap'],
                                       'parent': None
                                      },
                                      {
                                       'name': 'antlets/_templates/ubuntu-xenial@snap',
                                       'children': ['antlets/ant1', 'antlets/ant2', 'antlets/ant3'],
                                       'parent': 'antlets/_templates/ubuntu-xenial'
                                      },
                                      {
                                       'name': 'antlets/ant1',
                                       'children': [],
                                       'parent': 'antlets/_templates/ubuntu-xenial@snap'
                                      },
                                      {
                                       'name': 'antlets/ant2',
                                       'children': [],
                                       'parent': 'antlets/_templates/ubuntu-xenial@snap'
                                      },
                                      {
                                       'name': 'antlets/ant3',
                                       'children': [],
                                       'parent': 'antlets/_templates/ubuntu-xenial@snap'
                                      }]

        self.long_zfs_list = ["antlets\t-",
                        "antlets/Win10-base\tantlets/_templates/Win10@snap",
                        "antlets/Win10-base2\tantlets/_templates/Win10@snap",
                        "antlets/Win10-iso\tantlets/_templates/W10-1803-iso.kvm@1803",
                        "antlets/Win10-iso@sysprep\t-",
                        "antlets/Win10s\tantlets/_templates/Win10-1803-spc.kvm@1803",
                        "antlets/Win10s@uptodate\t-",
                        "antlets/_templates\t-",
                        "antlets/_templates/Blank\t-",
                        "antlets/_templates/Blank@snap\t-",
                        "antlets/_templates/Ubuntu16.04\t-",
                        "antlets/_templates/Ubuntu16.04@snap\t-",
                        "antlets/_templates/W10-1803-iso.kvm\tantlets/_templates/Blank@snap",
                        "antlets/_templates/W10-1803-iso.kvm@1803\t-",
                        "antlets/_templates/W10-1803-iso.kvm@snap\t-",
                        "antlets/_templates/Win10\t-",
                        "antlets/_templates/Win10@snap\t-",
                        "antlets/_templates/Win10-1803-spc.kvm\tantlets/_templates/Win10-Spice@snap",
                        "antlets/_templates/Win10-1803-spc.kvm@1803\t-",
                        "antlets/_templates/Win10-1803-spc.kvm@snap\t-",
                        "antlets/_templates/Win10-Spice\t-",
                        "antlets/_templates/Win10-Spice@snap\t-",
                        "antlets/_templates/ubuntu-xenial\t-",
                        "antlets/_templates/ubuntu-xenial@snap\t-",
                        "antlets/_tmp\t-",
                        "antlets/ant1\tantlets/_templates/ubuntu-xenial@snap",
                        "antlets/ant2\tantlets/_templates/ubuntu-xenial@snap",
                        "antlets/ant3\tantlets/_templates/ubuntu-xenial@snap",
                        "antlets/isos"]

    def test_create_dependency_list_returns_a_list(self):
        result = create_dependency_list(self.short_zfs_list)
        self.assertIsInstance(result, list)

    def test_create_dependency_list_returns_a_list_of_dicts(self):
        result = create_dependency_list(self.short_zfs_list)
        for item in result:
            self.assertIsInstance(item, dict)

    def test_create_dependency_list_each_dict_has_3_keys(self):
        result = create_dependency_list(self.short_zfs_list)
        for item in result:
            self.assertEqual(len(item), 3)

    def test_create_dependency_list_each_dict_children_key_is_a_list(self):
        result = create_dependency_list(self.short_zfs_list)
        for item in result:
            self.assertIsInstance(item['children'], list)

    def test_create_dependency_list(self):
        result = create_dependency_list(self.short_zfs_list)
        self.assertEqual(result, self.short_dependency_list)

    def test_create_json_list_returns_a_list(self):
        dlist = create_dependency_list(self.short_zfs_list)
        result = create_json_list(dlist)
        self.assertIsInstance(result, list)

    def test_create_json_list_each_item_is_a_dict(self):
        dlist = create_dependency_list(self.short_zfs_list)
        result = create_json_list(dlist)
        for item in result:
            self.assertIsInstance(item, dict)

        


if __name__ == '__main__':
    unittest.main()

