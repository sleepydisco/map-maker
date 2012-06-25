#!/usr/bin/env python
# encoding: utf-8
"""
directions.py

Created by David Wood on 2012-06-16.
Copyright (c) 2012 . All rights reserved.
"""

class Point(object):

    NORTH, NORTH_EAST, EAST, SOUTH_EAST, SOUTH, SOUTH_WEST, WEST, NORTH_WEST = range(8)   
    
    @staticmethod
    def opposite(p):
        return p + 4 if p < 4 else p - 4

    @staticmethod
    def left(p):
        return p - 1 if p > 0 else 7
        
    @staticmethod
    def right(p):
        return p + 1 if p < 7 else 0

class Direction(object):    

    __directions = {}
    
    def __init__(self, point, name_key, names={}):
        self.__point = point
        self.__name_key = name_key
        self.__names = names        
        Direction.__directions[point] = self
        
    def __repr__(self):
        return self.name()

    def point(self):
        return self.__point

    def name(self):
        if self.__name_key in self.__names:
           return self.__names[self.__name_key]
        return self.__name_key 
        
    def is_cardinal(self):
        return self.__point in (Point.NORTH, Point.EAST, Point.SOUTH, Point.WEST)
        
    def is_ordinal(self):
        return not self.is_cardinal()
        
    def opposite(self):
        return Direction.__directions[Point.opposite(self.point())]

    def neighbours(self):
        left = Point.left(self.point())
        right = Point.right(self.point())
        return (Direction.get(left), Direction.get(right))        
        
    def equivalents(self):
        (d1, d2) = self.neighbours()
        if self.is_ordinal():
            return ((d1, d2), (d2, d1))
        else:
            d3 = Direction.get(Point.left(d1.point()))
            d4 = Direction.get(Point.right(d2.point()))            
            return ((d2, d3), (d3, d2), (d1, d4), (d4, d1))
        
    @staticmethod
    def all():
        return map(lambda (k, v): v, sorted(Direction.__directions.iteritems()))
        
    @staticmethod
    def get(point):
        return Direction.__directions[point]

Direction(Point.NORTH, "n")
Direction(Point.SOUTH, "s")
Direction(Point.EAST, "e")
Direction(Point.WEST, "w")
Direction(Point.NORTH_EAST, "ne")
Direction(Point.NORTH_WEST, "nw")
Direction(Point.SOUTH_EAST, "se")
Direction(Point.SOUTH_WEST, "sw")
                          
def all():
    return Direction.all()

def main():
    print all()
    print Direction.get(Point.NORTH).equivalents()
    print Direction.get(Point.NORTH_WEST).equivalents()

if __name__ == '__main__':
    main()
        

