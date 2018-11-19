#!/usr/bin/python3

import unittest
import antlet_dependencies as ad


class TestAntletDependencies(unittest.TestCase):

    def test_get_zfs_list_returns_a_list(self):
        x = []
        result = ad.get_zfs_list()
        self.assertEqual(type(result), type(x))


if __name__ == '__main__':
    unittest.main()
