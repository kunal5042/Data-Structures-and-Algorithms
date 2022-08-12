# Question: https://leetcode.com/problems/number-of-ways-to-arrive-at-destination/

from typing import Optional, List

from heapq import heapify, heappop, heappush
class Node:
    def __init__(self, _id) -> 'Node':
        self.id = _id
        self.adjacents = set()
        
    def connect_with(self, node2, weight) -> None:
        """Connects node2 with self"""
        self.adjacents.add((weight, node2))
        
    def __lt__(self, other_node):
        """Compares other_node object with self for priority calculation"""
        return self.id < other_node.id
        
class Graph:
    def __init__(self, n: int, adj_list: 'List[[source, dest, weight]]') -> 'Graph':
        self.nodes = {}
        self.initialize_nodes(n)
        self.build_graph(adj_list)
        
    def initialize_nodes(self, node_count: int) -> None:
        """Creates node_count node objects"""
        for node_id in range(node_count):
            self.nodes[node_id] = Node(node_id)
    
    def build_graph(self, adj_list: 'List[[source, dest, weight]]') -> None:
        """Adds edges among nodes"""
        for (source, dest, time) in adj_list:
            self.nodes[source].connect_with(self.nodes[dest], time)
            self.nodes[dest].connect_with(self.nodes[source], time)
            
    def get_ways_to_reach_destination_in_shortest_time(self, source: 'node_id', dest: 'node_id'):
        """Returns the number of ways we can reach dest node from source node
        in shortest time.
        """
        # Using Dijkstra's Algorithm and Dynamic Programming
        dest_node = self.nodes[dest]
        
        # Priority Queue using binary-min-heap
        unexplored = [(0, self.nodes[source])]
        heapify(unexplored)
        
        # keep track of explored nodes in path-finding
        explored = set()
        
        # store the shortest time for each node from source
        times = [float('inf') for _ in range(len(self.nodes))]
        times[source] = 0
        
        # stores the number of ways we can reach each node from source
        # in shortest time
        ways = [0 for _ in range(len(self.nodes))]
        ways[source] = 1
        
        mod = (10**9) + 7        
        
        while len(unexplored) != 0:
            time, node = heappop(unexplored)
            
            if node in explored: continue
            explored.add(node)
            
            for adj_time, adj_node in node.adjacents:
                if adj_node in explored: continue
                
                new_discovered_time = time + adj_time
                
                # if this path's time is equal to shortest path
                # increment the number of ways we can reach this node
                # that is, number of ways we can reach before + 
                # number of ways we can reach the node from which we came to this
                if new_discovered_time == times[adj_node.id]:
                    ways[adj_node.id] += ways[node.id]
                    
                # if this path is shorter?
                # overwrite the number of ways we can reach this node in shortest path
                # with number of ways we can reach
                elif new_discovered_time < times[adj_node.id]:
                    ways[adj_node.id] = ways[node.id]
                    times[adj_node.id] = new_discovered_time
                    heappush(unexplored, (new_discovered_time, adj_node))
                    
        return ways[dest] % mod
        
class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        graph = Graph(n, roads)
        return graph.get_ways_to_reach_destination_in_shortest_time(0, n-1)
'''

# Kunal Wadhwa

'''