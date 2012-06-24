#!/usr/bin/env python
# encoding: utf-8
"""
test_map.py

Created by David Wood on 2012-06-24.
Copyright (c) 2012 . All rights reserved.
"""

import sys
import os


import unittest

from mapmaker.map import Location, Path

class TestLocation(unittest.TestCase):
    
    def test_location_has_id(self):
        loc = Location(1)
        self.assertEqual(loc.id(), 1)
    
class TestPath(unittest.TestCase):
    pass
