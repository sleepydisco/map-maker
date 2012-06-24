#!/usr/bin/env python
# encoding: utf-8
"""
directions.py

Created by David Wood on 2012-06-16.
Copyright (c) 2012 . All rights reserved.
"""

class Direction(object):
    
    NORTH = 0
    NORTH_EAST = 1
    EAST = 2
    SOUTH_EAST = 3
    SOUTH = 4
    SOUTH_WEST = 5
    WEST = 6
    NORTH_WEST = 7    

    def __init__(self, position, name, names={}):
        self.__position = position
        self.__name_key = name
        self.__names = names

    def __repr__(self):
        return self.name()

    def position(self):
        return self.__position

    def name(self):
        if self.__name_key in self.__names:
           return self.__names[self.__name_key]
        return self.__name_key 

_DIRECTIONS = [ Direction(Direction.NORTH, "n"),                
                Direction(Direction.NORTH_EAST, "ne"), 
                Direction(Direction.EAST, "e"), 
                Direction(Direction.SOUTH_EAST, "se"), 
                Direction(Direction.SOUTH, "s"), 
                Direction(Direction.SOUTH_WEST, "sw"), 
                Direction(Direction.WEST, "w"), 
                Direction(Direction.NORTH_WEST, "nw")]

class Directions(object):

    @staticmethod
    def all_directions():
        return _DIRECTIONS

    @staticmethod
    def opposite(direction):
        pos = direction.position()
        pos_opp = pos + 4 if pos < 4 else pos - 4
        return _DIRECTIONS[pos_opp]
        
    @staticmethod
    def neighbouring(direction):
        pos = direction.position()
        pos_left = pos - 1 if pos > 0 else 7
        pos_right = pos + 1 if pos < 7 else 0
        return (_DIRECTIONS[pos_left], _DIRECTIONS[pos_right])
        
    @staticmethod
    def equivalents(direction):
        pos = direction.position()
        pos_left = pos - 1 if pos > 0 else 7
        pos_right = pos + 1 if pos < 7 else 0
        pos_left2 = pos_left - 1 if pos_left > 0 else 7
        pos_right2 = pos_right + 1 if pos_right < 7 else 0
        d1 = _DIRECTIONS[pos_left]
        d2 = Directions.opposite(_DIRECTIONS[pos_left2])
        d3 = _DIRECTIONS[pos_right]
        d4 = Directions.opposite(_DIRECTIONS[pos_right2])
        
        return ((d1, d2), 
                (d3, d4),
                (d2, d1),
                (d4, d3))

def main():
    direction = _DIRECTIONS[0]
    print "Direction: {0} ".format(direction.name())    
    print "Opposite: {0} ".format(Directions.opposite(direction).name())    
    print "Neighbours: " + str(Directions.neighbouring(direction))
    print "Equivalents: " + str(Directions.equivalents(direction))
        

if __name__ == '__main__':
    main()
        

