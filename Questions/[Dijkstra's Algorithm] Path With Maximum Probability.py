# Question: https://leetcode.com/problems/path-with-maximum-probability/

from typing import Optional, List

from heapq import heapify, heappop, heappush
class Node:
    def __init__(self, label):
        self.label = label
        self.connected = set()
        
    def connect_with(self, node2, probability):
        """Connects self with node2 with a weighted edge"""
        self.connected.add((node2, probability))
        
    def __lt__(self, other_node):
        """Compares self with other_node: Node"""
        return self.label < other_node.label
        
    def __str__(self):
        """Returns the label of the node as a string"""
        return str(node.label)
    
    
class Graph:
    def __init__(self):
        self.nodes = {}
        self.total_nodes = 0
        
    def initialize_nodes(self, node_count):
        """Creates node_count number of nodes with labels [1-node_count]"""
        for label in range(node_count):
            self.nodes[label] = Node(label)
            
        self.total_nodes = len(self.nodes)
        
    def add_edges(self, edges):
        """Adds weighted edges among nodes from the information provided
        in the edges array
        """
        for (source, destination), probability in edges:
            self.nodes[source].connect_with(self.nodes[destination], probability)
            self.nodes[destination].connect_with(self.nodes[source], probability)
            
    def get_max_probability(self, source, destination):
        """Returns the probability of the best path from source to destination.
        Using Dijkstra's Shortest-Path Algorithm.
        """
        probabilities = [float('inf') for _ in range(self.total_nodes)]
        # representing weights as negative
        # so, instead of shortest path, we will get the longest path
        unexplored = [(-1.0, self.nodes[source])]
        heapify(unexplored)
        explored   = set()
        
        while len(unexplored) != 0:
            probab, node = heappop(unexplored)
            
            if node in explored: continue
                
            for adjacent, adj_probab in node.connected:
                prob_to_adjacent = -1 * abs(probab * adj_probab)
                
                print(node.label, adjacent.label, prob_to_adjacent)
                if probabilities[adjacent.label] > prob_to_adjacent:
                    probabilities[adjacent.label] = prob_to_adjacent
                    
                heappush(unexplored, (prob_to_adjacent, adjacent))
                
            explored.add(node)
            
        if probabilities[destination] == float('inf'): return 0.000
        return abs(probabilities[destination])
        
            
class Solution:
    # O((|V| + |E|) * log(V)) Time
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        graph = Graph()
        graph.initialize_nodes(n)
        graph.add_edges(zip(edges, succProb))
        return graph.get_max_probability(start, end)
'''

# Kunal Wadhwa

'''