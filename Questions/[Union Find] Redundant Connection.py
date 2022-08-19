# Question: https://leetcode.com/problems/redundant-connection/
# Medium
from typing import Optional, List

class Node:
    def __init__(self, value):
        self.val      = value
        self.children = set()
        
    def add_child(self, child):
        self.children.add(child)
        
class Graph:
    def __init__(self, edges):
        self.nodes = {}
        self.edges = edges
        self.build()
        
    def build(self):
        for edge in self.edges:
            node1, node2 = edge
            if node1 not in self.nodes:
                self.nodes[node1] = Node(node1)
            if node2 not in self.nodes:
                self.nodes[node2] = Node(node2)
            self.nodes[node1].add_child(self.nodes[node2])
            self.nodes[node2].add_child(self.nodes[node1])
    
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parents = [idx for idx in range(len(edges)+1)]
        ranks   = [1 for idx in range(len(edges)+1)]
        
        # Union-Find Algorithm
        def find(node: int) -> int:
            parent = parents[node]
            
            while parent != parents[parent]:
                parent = parents[parent]
                
            return parent
        
        def union(node1: int, node2: int) -> bool:
            parent1, parent2 = find(node1), find(node2)
            
            # union of these two nodes will form a cycle
            if parent1 == parent2:
                return False
            
            if ranks[parent1] > ranks[parent2]:
                parents[parent2] = parent1
                ranks[parent1] += ranks[parent2]
                
            else:
                parents[parent1] = parent2
                ranks[parent2] += ranks[parent1]
            
            return True
        
        
        for node1, node2 in edges:
            if not union(node1, node2):
                return [node1, node2]
            
        return
'''

# Kunal Wadhwa

'''