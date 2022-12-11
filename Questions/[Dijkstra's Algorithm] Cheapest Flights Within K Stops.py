# Question: https://leetcode.com/problems/cheapest-flights-within-k-stops/
# Medium
# Shortest path with an added constraint of max hops/nodes
from typing import Optional, List

from heapq import heapify, heappop, heappush
class Node:
    def __init__(self, label):
        self.label = label
        self.connected = set()
        
    def connect_with(self, node2, price):
        """Connects self with node2 with a weighted edge"""
        self.connected.add((node2, price))
        
    def __lt__(self, other_node):
        return self.label < other_node.label
        
    def __str__(self):
        return str(self.label)
    
    
class Graph:
    def __init__(self):
        self.nodes = {}
        self.total_nodes = 0
        
    def initialize_nodes(self, node_count):
        """Creates node_count number of nodes with labels 1-node_count"""
        for label in range(node_count):
            self.nodes[label] = Node(label)
            
        self.total_nodes = len(self.nodes)
        
    def add_edges(self, edges):
        """Adds weighted edges among nodes from the information provided
        in the edges array
        """
        for (source, destination, price) in edges:
            self.nodes[source].connect_with(self.nodes[destination], price)
        
    def cheapest_price_from(self, source, destination, max_stops) -> int:
        """Returns the minimum price a traveller has to pay if he/she
        wants to travel from city source to city destination with a maximum
        of max_stops in between
        """
        # using Dijktra's Algorithm
        explored_levels = [float('inf') for _ in range(self.total_nodes)]
        source_node, destination_node = self.nodes[source], self.nodes[destination]
        
        unexplored = [(0, source_node, 0)]
        heapify(unexplored)
        
        while len(unexplored) != 0:
            price, city, stops = heappop(unexplored)
            
            # Dijktra's greediness guarantees shortest path
            if city == destination_node: return price
                
            # if stops > max_stops, can't explore this path further
            # if stops >= explored_levels[city.label], the best route from this path was
            # already explored
            if stops > max_stops or stops >= explored_levels[city.label]:
                continue
                
            explored_levels[city.label] = stops 
                
            for stop, stop_price in city.connected:
                price_from_source = price + stop_price
                stops_from_source = stops + 1
                heappush(unexplored, (price_from_source, stop, stops_from_source))
            
        return -1
        
class Solution:
    # O((|V| + |E|) * log(V)) Time
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = Graph()
        graph.initialize_nodes(n)
        graph.add_edges(flights)
        return graph.cheapest_price_from(src, dst, k)

'''

# Kunal Wadhwa

'''