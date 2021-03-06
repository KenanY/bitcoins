#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
sys.path.insert(0, os.path.abspath('..'))
import bitcoins
import unittest


class BitcoinsTestSuite(unittest.TestCase):

    _multiprocess_can_split_ = True

    def test_get_difficulty(self):
        assert type(bitcoins.get_difficulty()) is float

    def test_get_block_count(self):
        assert type(bitcoins.get_block_count()) is int

    def test_latest_hash(self):
        assert type(bitcoins.get_latest_hash()) is str

    def test_get_block_hash(self):
        assert type(bitcoins.get_block_hash(1337)) is str

if __name__ == '__main__':
    unittest.main()
