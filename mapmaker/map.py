#!/usr/bin/env python
# encoding: utf-8
"""
map.py

Created by David Wood on 2012-06-12.
Copyright (c) 2012 . All rights reserved.
"""

import sys
import os

from graph import Node, Edge
from directions import Directions

class Location(Node):    
        
    def __init__(self, id_):
        super(Location, self).__init__(id_)
        self.__paths = {} # direction -> Node
      
    def add_path(self, path, direction):
        self.__paths[direction] = path       
        self.add_edge(path)
        
    def path_exists(self, direction):
        return direction in self.__paths
        
    def get_path(self, direction):
        if self.path_exists(direction):
            return self.__paths[direction]        
        return None
        
    def get_location_in(self, direction):
        path = self.get_path(direction)
        if path:
            return path.get_pair_for(self)
        return None
        
    def display_paths(self):
        for direction, path in self.__paths.iteritems():
            print " {0} to {1}".format(direction, path.get_pair_for(self))
                        
class Path(Edge):
    pass

class Map(object):

    def __init__(self, origin=None):
        self.__locations = [origin]
        self.__paths = []

    def add_location(self, location):
        self.__locations.append(location)

    def add_path(self, path):
        self.__paths.append(path)

    def origin(self):
        return self.__locations[0]

    def locations(self):
        return self.__locations

    def find_location_from_equivalent_direction(self, location, direction):
        print "  Attempting to look at equivalent directions..."
        found = None
        for (first_direction, second_direction) in Directions.equivalents(direction):
            print "  Going {0} then {1} from {2}".format(first_direction, second_direction, location)
            first_location = location.get_location_in(first_direction)
            if first_location:
                print "  Got to {0} by going {1}".format(first_location, first_direction)
                found = first_location.get_location_in(second_direction)
                if found: 
                    print "  ** Found: {0}".format(found)
                    break
        return found                

    def paths(self):
        return self.__paths

class IdGenerator(object):
    def __init__(self, next=0):
        self.__next = 0
        
    def next(self):
        next = self.__next
        self.__next += 1
        return next

class PathStrategy(object):
        
    def directions(self, location=None):
        """Returns a list of directions that the Location could have"""
        return Directions.all_directions()
    
class MapBuilder(object):

    def __init__(self, num_locations=8, path_strategy=PathStrategy(), id_generator=IdGenerator()):
        self.num_locations = num_locations
        self.__id_generator = id_generator
        self.__path_strategy = path_strategy
        self.__location_queue = []
        self.__map = None

    def _next_location(self):
        """Returns the next Location to be processed, or None if none exists"""
        if len(self.__location_queue) > 0:
            return self.__location_queue.pop(0)
        return None

    def _new_location(self):
        """Creates a new Location. This does not add the Location to the map"""
        return Location(self.__id_generator.next())

    def _visit_next_location(self):
        """Visits the next Location from the queue"""
        next_location = self._next_location()
        if next_location: 
            self._visit(next_location)
            
    def _discover_location_in_direction_via_neighbours(self, location, direction):
        pass
            
    def _visit(self, location):
        print "Visting {0}".format(location)
        for direction in self.__path_strategy.directions(location):
            print "Going in direction {0} from {1}".format(direction, location)
            if not location.path_exists(direction):
                to_location = self.__map.find_location_from_equivalent_direction(location, direction)
                print "Found: {0}".format(to_location)
                if not to_location and len(self.__map.locations()) < self.num_locations:
                    to_location = self._new_location()   
                    self.__map.add_location(to_location)
                    self.__location_queue.append(to_location)
                    print "** Created new location {0}".format(to_location)
                if to_location:
                    path = Path(location, to_location)
                    print "Created new path {0}".format(path)                 
                    
                    print "Adding path to {0} in direction {1} from {2}".format(to_location, direction, location)
                    location.add_path(path, direction)
                    print "Adding path to {0} in direction {1} from {2}".format(location, Directions.opposite(direction), to_location)
                    to_location.add_path(path, Directions.opposite(direction))
                                        
                    self.__map.add_path(path)
        self._visit_next_location()
                
    def build(self):
        self.__map = Map(self._new_location())
        self._visit(self.__map.origin())
        return self.__map               
               
def main():
    builder = MapBuilder()
    map_ = builder.build()

    for location in map_.locations():
        print "Location: {0}".format(location)
        location.display_paths()


if __name__ == '__main__':
    main()

