# Question: https://leetcode.com/problems/cheapest-flights-within-k-stops/

from typing import Optional, List

class Node:
    def __init__(self, label):
        self.label = label
        self.connected = set()
        
    def connect_with(self, node2, price):
        """Connects self with node2 with a weighted edge"""
        self.connected.add((node2, price))
        
    def __str__(self):
        return str(node.label)
    
    
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
        # using Dijktra's Algorithm
        explored = set()
        prices = [(float('inf'), float('inf')) for _ in range(self.total_nodes)]
        prices[source] = (0, k)
        
        source_node, destination_node = self.nodes[source], self.nodes[destination]
        
        for dest_city, dest_city_price in source_node.connected:
            prices[dest_city.label] = (dest_city_price, 0)
            

        def next_cheapest_stop() -> tuple[Node, int, int]:
            """Among the cities that are not yet explored.
            Returns the city node and it's price for which price is cheapest.
            """
            cheapest_stop, cheapest_stop_price = None, float('inf')
            stops_from_source = None
            
            for city, (price, stops) in enumerate(prices):
                node = self.nodes[city]
                if node in explored : continue
                if stops > max_stops: continue
                if price < cheapest_stop_price:
                    cheapest_stop = node
                    cheapest_stop_price = price
                    stops_from_source = stops - 1
                    
            return (cheapest_stop, cheapest_stop_price, stops_from_source)
        
        while len(explored) != self.total_nodes:
            # price = price to reach from root/source to this city
            # stops = stops to reach from root/source to this city
            city, price, stops = next_cheapest_stop()
            
            # explored all options
            if price == float('inf'): break
                
            for stop, stop_price in city.connected:
                price_from_source = price + stop_price
                stops_from_source = stops + 1
                
                (best_price_known, min_stops_known) = prices[stop.label]
                
                if stops_from_source < min_stops_known:
                    prices[stop.label] = (price_from_source, stops_from_source)
                    
                elif stops_from_source == min_stops_known:
                    if price_from_source < best_price_known:
                        prices[stop.label] = (price_from_source, stops_from_source)
                    
            explored.add(city)
            
            
        cheapest_price_to_destination, stops_to_destination = prices[destination]
        if cheapest_price_to_destination == float('inf'): return -1
        return cheapest_price_to_destination
        
        
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = Graph()
        graph.initialize_nodes(n)
        graph.add_edges(flights)
        return graph.cheapest_price_from(src, dst, k)
'''

# Kunal Wadhwa

'''