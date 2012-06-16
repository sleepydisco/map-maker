#!/usr/bin/env python
# encoding: utf-8
"""
map.py

Created by David Wood on 2012-06-12.
Copyright (c) 2012 . All rights reserved.
"""

import sys
import os

class Direction(object):
    NORTH = 0
    NORTH_EAST = 1
    EAST = 2
    SOUTH_EAST = 3
    SOUTH = 4
    SOUTH_WEST = 5
    WEST = 6
    NORTH_WEST = 7    

    DIRECTIONS = list([Direction(0, "n"), Direction(1, "ne"), Direction(2, "e"), Direction(3, "se"), Direction(4, "s"), Direction(5, "sw"), Direction(6, "w"), Direction(7, "nw")])

    def __init__(self, value, name):
        self.value = value
        self.name = name

    def __repr__(self):
        return "{0} [{1}]".format(self.name, self.value)

    @staticmethod
    def values():
        return [] #Direction.DIRECTIONS
        
    def opposite(self):
        pass

class Tile(object):    
    UNASSIGNED = None
        
    def __init__(self):
        self.edges = {}
        for edge in Tile.DIRECTIONS:
            self.edges[edge.value] = Tile.UNASSIGNED        

def main():
    t = Tile()
    print t.edges


if __name__ == '__main__':
	main()

