#!/usr/bin/env python
# encoding: utf-8
"""
graph.py

Created by David Wood on 2012-06-17.
Copyright (c) 2012 . All rights reserved.
"""

import sys
import os

class Node(object):
    
    def __init__(self, id):
        self.__id = id
        self.__edges = []
        
    def id(self):
        return self.__id    
        
    def __repr__(self):
        return "Node[{0}]".format(self.__id)
        
    def __eq__(self, other):
        return self.__id == other.__id
        
    def add_edge(self, edge):
        self.__edges.append(edge)

class Edge(object):

    def __init__(self, a, b):            
        self.points = _order_nodes(a, b)
        self.bidirectional= True

    def __eq__(self, other):
        return self.points == other.points    

    def __repr__(self):
        return str(self.points)

    def get_pair_for(self, item):
        for point in self.points:
            if point != item:
                return point
        return None

def _order_nodes(a, b):
    for node in (a, b):
        if not hasattr(node, 'id'):
            raise TypeError("{0} needs an id".format(node))
            
    if a.id() < b.id():
        return (a, b)
    else:
        return (b, a)        
    
def main():
    pass

if __name__ == '__main__':
    main()

