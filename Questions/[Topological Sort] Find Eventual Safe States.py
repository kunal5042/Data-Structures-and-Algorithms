# Question: https://leetcode.com/problems/find-eventual-safe-states/
# Medium

class Graph:
    def __init__(self, adj_list):
        self.nodes = {}
        self.build_graph(adj_list)

    def init_nodes(self, node_count):
        for idx in range(node_count):
            self.nodes[idx] = set()

    def add_directed_edge(self, _from, _to):
        self.nodes[_from].add(_to)
    
    def link_nodes(self, adj_list):
        for from_node in range(len(adj_list)):
            for to_node in adj_list[from_node]:
                self.add_directed_edge(from_node, to_node)
    
    def build_graph(self, adj_list):
        self.init_nodes(len(adj_list))
        self.link_nodes(adj_list)

class SafeNodes:
    def __init__(self, graph):
        self.safe_nodes = set()
        self.non_safe_nodes = set()
        self.recursion_call_stack = set()
        self.graph = graph

    def mark_nodes(self, node):
        if node in self.recursion_call_stack or node in self.non_safe_nodes:
            return False
        
        if node in self.safe_nodes:
            return True
        
        self.recursion_call_stack.add(node)
        is_node_safe = True
        
        for neighbor in self.graph[node]:
            if neighbor in self.safe_nodes:
                continue

            if neighbor in self.non_safe_nodes:
                is_node_safe = False

            if self.mark_nodes(neighbor) is False:
                is_node_safe = False

        if is_node_safe is True:
            self.safe_nodes.add(node)
        else:
            self.non_safe_nodes.add(node)

        self.recursion_call_stack.remove(node)
        return is_node_safe
    
    def mark_terminals(self):
        for node_id in range(len(self.graph)):
            if len(self.graph[node_id]) == 0:
                self.safe_nodes.add(node_id)
    
    def get_safe_nodes(self):
        self.mark_terminals()
        for node_id in range(len(self.graph)):
            self.mark_nodes(node_id)

        return sorted(list(self.safe_nodes))


from typing import List

class Solution:
    # O(n + m) time and space
    # where 
    # n --> number of nodes
    # m --> number of edges
    #
    def eventualSafeNodes(self, adj_list: List[List[int]]) -> List[int]:
        graph = Graph(adj_list).nodes
        sf_helper = SafeNodes(graph)
        return sf_helper.get_safe_nodes()


# July 14, 2023

'''

# Kunal Wadhwa

'''