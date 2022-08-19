# Question: https://leetcode.com/problems/min-cost-to-connect-all-points/
# Medium
from typing import Optional, List

from heapq import heapify as heap, heappop as hpop, heappush as hpush
class Node:
    def __init__(self, x: 'int', y: 'int') -> 'Node':
        self.x = x
        self.y = y
        self.adjacents = set()
        
    def manhattan(self, other_node: 'Node') -> 'int':
        x2, y2 = other_node.x, other_node.y
        return abs(self.x - x2) + abs(self.y - y2)
    
    def add_adjacent(self, adj_node: 'Node') -> 'None':
        weight = self.manhattan(adj_node)
        self.adjacents.add((weight, adj_node))
        
    def __lt__(self, other_node: 'Node') -> 'bool':
        return len(self.adjacents) > len(other_node.adjacents) 
        
class Graph:
    def __init__(self, points: '[[int, int], ..]') -> 'Graph':
        self.nodes = {}
        self.init_nodes(points)
        self.build_graph(points)
        
    def init_nodes(self, points: '[[int, int], ..]') -> 'None':
        for x, y in points: self.nodes[(x,y)] = Node(x,y)
            
    def build_graph(self, points: '[[int, int], ..]') -> 'None':
        # creating a connected, weighted, undirected graph
        for idx in range(len(points)):
            x1, y1 = points[idx]
            
            for jdx in range(idx+1, len(points)):
                x2, y2 = points[jdx]
                
                self.nodes[(x1, y1)].add_adjacent(self.nodes[(x2, y2)])
                self.nodes[(x2, y2)].add_adjacent(self.nodes[(x1, y1)])
                
    def min_cost_to_all_points(self, source: '(x, y)') -> 'int':
        # Prim's Algorithm
        unexplored = [(0, self.nodes[source])]
        heap(unexplored)
        min_span_tree = set()
        min_cost = 0
        
        # as long as not all nodes are included in the minimum spanning tree
        while len(min_span_tree) != len(self.nodes):
            cost, snode = hpop(unexplored)
            
            if snode in min_span_tree: continue
            min_span_tree.add(snode)
            
            # pick the best edge from the nodes that are not yet included
            # in the minimum spanning tree
            min_cost += cost
            
            for weight, adj_node in snode.adjacents:
                if adj_node in min_span_tree: continue
                    
                # if node not in minimum spanning tree
                hpush(unexplored, (weight, adj_node))
                
        return min_cost
                
class Solution:
    # O((|V| + |E|) * log(V)) Time
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        graph = Graph(points)
        source = (points[0][0], points[0][1])
        return graph.min_cost_to_all_points(source)
'''

# Kunal Wadhwa

'''