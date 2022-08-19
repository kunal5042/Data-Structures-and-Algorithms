# Question: https://leetcode.com/problems/evaluate-division/
# Medium
from typing import Optional, List

class Node:
    def __init__(self, label):
        self.label = label
        self.connected = set()
        
class Graph:
    def __init__(self):
        self.nodes = {}
        
    def build(self, equations, values):
        """Builds the graph"""
        for variables, value in zip(equations, values):
            A, B = variables
                        
            if A not in self.nodes: self.nodes[A] = Node(A)
            if B not in self.nodes: self.nodes[B] = Node(B)
                
            # adding a weighted directed edge from A ----> B and B ----> A
            self.nodes[A].connected.add((self.nodes[B], value))
            self.nodes[B].connected.add((self.nodes[A], 1/value))
            
    def cost_to_node(self, start, destination):
        """Given two nodes, if a path exists from start to destination.
        Returns the cost of this path, otherwise returns -1.0
        """
        visited = set()
        queue = deque([(start, 1)])
        while len(queue):
            node, cost = queue.popleft()
            
            # reached destination
            if node == destination:
                return cost
            
            visited.add(node)
            
            for neighbor, its_cost in node.connected:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, cost * its_cost))
                    
        # path from start to destination doesn't exist
        return -1.0
            
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # initializing the graph
        graph = Graph()
        graph.build(equations, values)
        
        result = []
        
        for C, D in queries:
            start, destination = C, D
            
            # path from start to destination can't exist if any of the two nodes are not present
            if start not in graph.nodes or destination not in graph.nodes:
                result.append(-1.0)
                continue
                
            result.append(graph.cost_to_node(graph.nodes[start], graph.nodes[destination]))
            
        return result
'''

# Kunal Wadhwa

'''
