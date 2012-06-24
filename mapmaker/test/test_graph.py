#!/usr/bin/env python
# encoding: utf-8
"""
graph-test.py

Created by David Wood on 2012-06-17.
Copyright (c) 2012 . All rights reserved.
"""

import sys
import os

import unittest

from mapmaker.graph import Node, Edge

NODE_ONE = Node(1)
NODE_TWO = Node(2)

def an_edge_with_nodes(a, b):
    return Edge(a, b)

class TestEdge(unittest.TestCase):

    def test_edge_without_second_node_fails(self):   
        try:
            an_edge_with_nodes(NODE_ONE, 2)
            self.fail()
        except: 
            pass
        
    def test_edge_without_first_node_fails(self):   
        try:
            an_edge_with_nodes(1, NODE_TWO)
            self.fail()
        except: 
            pass
        
    def test_cannot_create_edge_betweeen_nodes_with_same_id(self):
        try:
            an_edge_with_nodes(NODE_ONE, Node(1))
        except:
            pass    

    def test_cannot_create_edge_betweeen_same_node(self):
        try:
            an_edge_with_nodes(NODE_ONE, NODE_ONE)
        except:
            pass    
        
    def test_edge_equivalence(self):   
        self.assertEqual(an_edge_with_nodes(NODE_ONE, NODE_TWO), an_edge_with_nodes(NODE_ONE, NODE_TWO))

    def test_edge_equivalence_when_edges_are_not_equal(self):   
        self.assertNotEqual(an_edge_with_nodes(NODE_ONE, NODE_TWO), an_edge_with_nodes(Node(3), Node(4)))

    def test_edge_equivalence_different_order(self):   
        self.assertEqual(an_edge_with_nodes(NODE_ONE, NODE_TWO), an_edge_with_nodes(NODE_TWO, NODE_ONE))
        
class TestNode(unittest.TestCase):
    
    def test_node_equivalence_when_nodes_are_equal(self):
        self.assertEqual(NODE_ONE, Node(1))
        
    def test_node_equivalence_when_nodes_are_not_equal(self):
        self.assertNotEqual(NODE_ONE, NODE_TWO)
