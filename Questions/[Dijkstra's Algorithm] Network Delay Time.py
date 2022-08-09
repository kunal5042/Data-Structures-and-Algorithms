# Question: https://leetcode.com/problems/network-delay-time/

from typing import Optional, List

class Node:
    def __init__(self, label):
        self.label = label
        self.connected = set()
        
    def connect_with(self, node2, distance):
        """Connects self with node2 with a weighted edge"""
        self.connected.add((node2, distance))
        
    def __str__(self):
        return str(node.label)
    
    
class Graph:
    def __init__(self):
        self.nodes = {}
        self.total_nodes = 0
        
    def initialize_nodes(self, node_count):
        """Creates node_count number of nodes with labels 1-node_count"""
        for label in range(1, node_count+1):
            self.nodes[label] = Node(label)
            
        self.total_nodes = len(self.nodes)
            
    def add_edges(self, edges):
        """Adds weighted edges among nodes from the information provided
        in the edges array
        """
        for (source, destination, distance) in edges:
            self.nodes[source].connect_with(self.nodes[destination], distance)
            
    def get_shortest_path_from(self, root_label) -> List[int]:
        """Returns a list of distances from node with label root_label to all other nodes"""
        explored = set()
        
        root_node = self.nodes[root_label]
        distances = [float('inf') for _ in range(self.total_nodes)]
        distances[root_label-1] = 0
        for (node, distance) in root_node.connected:
            distances[node.label-1] = distance
            
        def get_closest_unexplored_node() -> tuple[int, int]:
            """Returns the closest node and it's distance from the root"""
            closest_node, closest_node_distance = None, float('inf')
            
            for (label, distance) in enumerate(distances):
                node = self.nodes[label+1]
                if node in explored: continue
                if distance < closest_node_distance:
                    closest_node_distance = distance
                    closest_node = node
                    
            return (closest_node, closest_node_distance)
        
        while len(explored) != self.total_nodes:
            new_source, distance_to_new_source_from_root = get_closest_unexplored_node()
            
            # explored all possible paths
            if distance_to_new_source_from_root == float('inf'): break
                
            for adjacent, adjacent_distance in new_source.connected:
                if adjacent in explored: continue
                
                # update distance
                new_distance = distance_to_new_source_from_root + adjacent_distance
                if new_distance < distances[adjacent.label-1]:
                    distances[adjacent.label-1] = new_distance
                    
            # mark as explored
            explored.add(new_source)
            
        return distances
        
class Solution:
# O(V^2) Time (can be reduced to O(V + (E * log(V)) by using min-priority queue)
# O(V) Space
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = Graph()
        graph.initialize_nodes(n)
        graph.add_edges(times)
        farthest_distance = max(graph.get_shortest_path_from(k))
        return farthest_distance if farthest_distance != float('inf') else -1
'''

# Kunal Wadhwa

'''