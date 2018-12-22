#!/usr/bin/python3


import unittest
from zfs_dependencies import *


class TestAntletDependencies(unittest.TestCase):

    def setUp(self):

            
        self.zfs_nolist = [ 'antlets\t-',
                        'antlets/_templates\t-',
                        'antlets/_templates/Win10\t-',
                        'antlets/_templates/Win10@snap\t-',
                        'antlets/_templates/ubuntu-xenial\t-',
                        'antlets/_templates/ubuntu-xenial@snap\t-',
                        'antlets/win1\tantlets/_templates/Win10@snap',
                        'antlets/win2\tantlets/_templates/Win10@snap',
                        'antlets/ubu1\tantlets/_templates/ubuntu-xenial@snap',
                        'antlets/ubu2\tantlets/_templates/ubuntu-xenial@snap',
                        'antlets/_tmp\t-'
                      ]

        self.long_zfs_dlist = [ { 'name': 'antlets',
                        'parent': None,
                        'children': []},
                      { 'name': 'antlets/_templates',
                        'parent': None,
                        'children': []},
                      { 'name': 'antlets/_templates/Win10',
                        'parent': None,
                        'children': ['antlets/_templates/Win10@snap']},
                      { 'name': 'antlets/_templates/Win10@snap',
                        'parent': 'antlets/_templates/Win10',
                        'children': ['antlets/win1', 'antlets/win2']},
                      { 'name': 'antlets/_templates/ubuntu-xenial',
                        'parent': None,
                        'children': ['antlets/_templates/ubuntu-xenial@snap']},
                      { 'name': 'antlets/_templates/ubuntu-xenial@snap',
                        'parent': 'antlets/_templates/ubuntu-xenial',
                        'children': ['antlets/ubu1', 'antlets/ubu2']},
                      { 'name': 'antlets/win1',
                        'parent': 'antlets/_templates/Win10@snap',
                        'children': []},
                      { 'name': 'antlets/win2',
                        'parent': 'antlets/_templates/Win10@snap',
                        'children': []},
                      { 'name': 'antlets/ubu1',
                        'parent': 'antlets/_templates/ubuntu-xenial@snap',
                        'children': []},
                      { 'name': 'antlets/ubu2',
                        'parent': 'antlets/_templates/ubuntu-xenial@snap',
                        'children': []},
                      { 'name': 'antlets/_tmp',
                        'parent': None,
                        'children': []}
                    ]




    def test_create_dependency_list_returns_a_list(self):
        result = create_dependency_list(self.zfs_nolist)
        self.assertIsInstance(result, list)

    def test_create_dependency_list_returns_a_list_of_dicts(self):
        result = create_dependency_list(self.zfs_nolist)
        for item in result:
            self.assertIsInstance(item, dict)

    def test_create_dependency_list_each_dict_has_3_keys(self):
        result = create_dependency_list(self.zfs_nolist)
        for item in result:
            self.assertEqual(len(item), 3)

    def test_create_dependency_list_each_dict_children_key_is_a_list(self):
        result = create_dependency_list(self.zfs_nolist)
        for item in result:
            self.assertIsInstance(item['children'], list)

    def test_create_dependency_list(self):
        result = create_dependency_list(self.zfs_nolist)
        self.assertEqual(result, self.long_zfs_dlist)

    def test_create_json_list_returns_a_list(self):
        dlist = create_dependency_list(self.zfs_nolist)
        result = create_json_list(dlist)
        self.assertIsInstance(result, list)

    def test_create_json_list_each_item_is_a_dict(self):
        dlist = create_dependency_list(self.zfs_nolist)
        result = create_json_list(dlist)
        for item in result:
            self.assertIsInstance(item, dict)

    def test_create_json_list_each_dict_has_2_keys(self):
        dlist = create_dependency_list(self.zfs_nolist)
        result = create_json_list(dlist)
        for item in result:
            self.assertEqual(len(item), 2)
        


if __name__ == '__main__':
    unittest.main()

