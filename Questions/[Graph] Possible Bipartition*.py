# Question: https://leetcode.com/problems/possible-bipartition/
# Medium
from typing import Optional, List

class Node:
    def __init__(self, val):
        self.val = val
        self.children = set()
        
    def add_child(self, child):
        self.children.add(child)
        
class Graph:
    def __init__(self):
        self.graph = {}
        
    def build(self, dislikes):
        for ai, bi in dislikes:
            if ai not in self.graph: self.graph[ai] = Node(ai)
            if bi not in self.graph: self.graph[bi] = Node(bi)
                
            # undirected graph
            self.graph[ai].add_child(self.graph[bi])
            self.graph[bi].add_child(self.graph[ai])
            
    def can_group(self):
        # dividing into two groups
        groups = {"Group-1": set(), "Group-2": set()}
        # marks if a node has been grouped
        grouped = set()
        
        # checks, if we can group node and it's children
        # given they don't like it each other
        def depth_first_satisfy(node, alotted_group):
            if node in grouped:
                # if a node has been grouped
                # but
                # it's not present in it's alotted group
                if node not in groups[alotted_group]:
                    return False
                
            else:
                # add node to it's alotted group
                groups[alotted_group].add(node)
                # mark it as grouped
                grouped.add(node)
                
                # alot group to children
                alotted_group = "Group-1" if alotted_group != "Group-1" else "Group-2"

                for child in node.children:
                    # recursively perform for child
                    if depth_first_satisfy(child, alotted_group) is False:
                        return False
                    
            return True
        
        # perform grouping on all nodes
        for node, node_object in self.graph.items():
            if node_object not in grouped:
                if depth_first_satisfy(node_object, "Group-1") is False:
                    return False

        return True

class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        if len(dislikes) == 0: return True
        
        # initialize
        graph = Graph()
        # build
        graph.build(dislikes)
        # check
        return graph.can_group()


'''

# Kunal Wadhwa

'''
