# Question: https://leetcode.com/problems/all-paths-from-source-to-target/

from typing import Optional, List

class Node:
    def __init__(self, _id) -> 'Node':
        self.id = _id
        self.adjacents = set()
        
    def connect_with(self, node2) -> None:
        self.adjacents.add(node2)
        
class DAG:
    def __init__(self, adj_list) -> 'DAG':
        self.nodes = {}
        self.build_graph(adj_list)
        
    def build_graph(self, adj_list) -> None:
        for idx, adjacents in enumerate(adj_list):
            if idx not in self.nodes: self.nodes[idx] = Node(idx)
            for adj in adjacents:
                if adj not in self.nodes: self.nodes[adj] = Node(adj)
                self.nodes[idx].connect_with(self.nodes[adj])
    
class Solution:
    # O(V + E) Time and O(V) Space
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        _graph = DAG(graph)
        source = _graph.nodes[0]
        dest   = _graph.nodes[len(graph)-1]
        paths = []
        
        def find_paths(path, node):
            if node == dest:
                paths.append(path.copy())
                return
            
            for adj_node in node.adjacents:
                path.append(adj_node.id)
                find_paths(path, adj_node)
                path.pop()
                
        find_paths([0], source)
        return paths
            
'''

# Kunal Wadhwa

'''