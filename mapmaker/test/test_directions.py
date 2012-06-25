#!/usr/bin/env python
# encoding: utf-8
"""
test_Direction.py

Created by David Wood on 2012-06-25.
Copyright (c) 2012 . All rights reserved.
"""

import sys
import os

import unittest

from mapmaker.directions import Direction, Point

class TestDirection(unittest.TestCase):
        
    def test_equivalents_north(self):
        equivalents = Direction.get(Point.NORTH).equivalents()
        self.assertEquals(len(equivalents), 4)
        self.assertIn((Direction.get(Point.WEST), Direction.get(Point.NORTH_EAST)), equivalents)
        self.assertIn((Direction.get(Point.EAST), Direction.get(Point.NORTH_WEST)), equivalents)
        self.assertIn((Direction.get(Point.NORTH_WEST), Direction.get(Point.EAST)), equivalents)
        self.assertIn((Direction.get(Point.NORTH_EAST), Direction.get(Point.WEST)), equivalents)

    def test_equivalents_south(self):
        equivalents = Direction.get(Point.SOUTH).equivalents()
        self.assertEquals(len(equivalents), 4)
        self.assertIn((Direction.get(Point.WEST), Direction.get(Point.SOUTH_EAST)), equivalents)
        self.assertIn((Direction.get(Point.EAST), Direction.get(Point.SOUTH_WEST)), equivalents)
        self.assertIn((Direction.get(Point.SOUTH_WEST), Direction.get(Point.EAST)), equivalents)
        self.assertIn((Direction.get(Point.SOUTH_EAST), Direction.get(Point.WEST)), equivalents)

    def test_equivalents_west(self):
        equivalents = Direction.get(Point.WEST).equivalents()
        self.assertEquals(len(equivalents), 4)
        self.assertIn((Direction.get(Point.SOUTH), Direction.get(Point.NORTH_WEST)), equivalents)
        self.assertIn((Direction.get(Point.NORTH), Direction.get(Point.SOUTH_WEST)), equivalents)
        self.assertIn((Direction.get(Point.SOUTH_WEST), Direction.get(Point.NORTH)), equivalents)
        self.assertIn((Direction.get(Point.NORTH_WEST), Direction.get(Point.SOUTH)), equivalents)
        
    def test_equivalents_east(self):
        equivalents = Direction.get(Point.EAST).equivalents()
        self.assertEquals(len(equivalents), 4)
        self.assertIn((Direction.get(Point.SOUTH), Direction.get(Point.NORTH_EAST)), equivalents)
        self.assertIn((Direction.get(Point.NORTH), Direction.get(Point.SOUTH_EAST)), equivalents)
        self.assertIn((Direction.get(Point.SOUTH_EAST), Direction.get(Point.NORTH)), equivalents)
        self.assertIn((Direction.get(Point.NORTH_EAST), Direction.get(Point.SOUTH)), equivalents)
        
    def test_equivalents_north_west(self):
        equivalents = Direction.get(Point.NORTH_WEST).equivalents()
        self.assertEquals(len(equivalents), 2)
        self.assertIn((Direction.get(Point.NORTH), Direction.get(Point.WEST)), equivalents)
        self.assertIn((Direction.get(Point.WEST), Direction.get(Point.NORTH)), equivalents)

    def test_equivalents_north_east(self):
        equivalents = Direction.get(Point.NORTH_EAST).equivalents()
        self.assertEquals(len(equivalents), 2)
        self.assertIn((Direction.get(Point.NORTH), Direction.get(Point.EAST)), equivalents)
        self.assertIn((Direction.get(Point.EAST), Direction.get(Point.NORTH)), equivalents)
                


