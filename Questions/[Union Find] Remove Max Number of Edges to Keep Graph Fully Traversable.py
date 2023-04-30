# Question: https://leetcode.com/problems/remove-max-number-of-edges-to-keep-graph-fully-traversable/
# Hard

class UnionFind:
    def __init__(self, number_of_nodes):
        self.parent = list(range(number_of_nodes+1))
        self.rank = [0] * (number_of_nodes+1)
        self.components = number_of_nodes

    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, node_u, node_v):
        representative_u = self.find(node_u)
        representative_v = self.find(node_v)
        
        if representative_u == representative_v:
            return False
        
        if self.rank[representative_u] < self.rank[representative_v]:
            self.parent[representative_u] = representative_v
            self.rank[representative_v] += self.rank[representative_u]
        else:
            self.parent[representative_v] = representative_u
            self.rank[representative_u] += self.rank[representative_v]
            
        self.components -= 1
        return True
    
    def is_present(self, node_u, node_v):
        return self.find(node_u) == self.find(node_v)

    def get_rank(self, node):
        return self.rank[self.find(node)]
    
from typing import List
import copy

class Solution:
    #
    # Time O(e * alpha(n)) and Space O(n)
    # where 
    # n = number of nodes
    # e = number of edges
    # 
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        uf_alice = UnionFind(n)
        required = 0
        
        for (_type, node_u, node_v) in edges:
            if _type != 3: continue
            required += int(uf_alice.union(node_u, node_v))
            
        uf_bob = copy.deepcopy(uf_alice)
        
        for (_type, node_u, node_v) in edges:
            if _type == 3: continue
            if _type == 1: required += int(uf_alice.union(node_u, node_v))
            if _type == 2: required += int(uf_bob.union(node_u, node_v))
                
        if uf_alice.components != 1: return -1
        if uf_bob.components   != 1: return -1
        
        can_remove = len(edges) - required
        return can_remove if can_remove >= 0 else -1


# April 30, 2023

'''

# Kunal Wadhwa

'''