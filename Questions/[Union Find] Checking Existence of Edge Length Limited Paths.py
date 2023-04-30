# Question: https://leetcode.com/problems/checking-existence-of-edge-length-limited-paths/
# Hard

class UnionFind:
    def __init__(self, number_of_nodes):
        self.parent = list(range(number_of_nodes))
        self.rank = [0] * number_of_nodes

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
            
        return True

    def get_rank(self, node):
        return self.rank[self.find(node)]

from collections import defaultdict
from typing import List

class Solution:
    # time limit exceeded
    def distanceLimitedPathsExist(self, n: int, edge_list: List[List[int]], queries: List[List[int]]) -> List[bool]:
        def build_graph(n, edge_list):
            graph = defaultdict(set)
            distances = {}
            for node_u, node_v, dist in edge_list:
                graph[node_u].add(node_v)
                graph[node_v].add(node_u)
                edge1 = (node_u, node_v)
                edge2 = (node_v, node_u)
                if edge1 not in distances: distances[edge1] = dist
                if edge2 not in distances: distances[edge2] = dist
                distances[edge1] = min(distances[edge1], dist)
                distances[edge2] = min(distances[edge2], dist)
            return graph, distances

        graph, distances = build_graph(n, edge_list)
        output = [False for _ in range(len(queries))]

        def resolve(node, max_distance, destination, visited):
            if node == destination:
                return True
            visited.add(node)
            for neighbor in graph[node]:
                if distances[(node, neighbor)] >= max_distance: continue
                if neighbor in visited: continue
                if resolve(neighbor, max_distance, destination, visited) is True:
                    return True
            return False

        for query_no, (node_u, node_v, limit_distance) in enumerate(queries):
            if resolve(node_u, limit_distance, node_v, set()) is True:
                output[query_no] = True

        return output

    # Time  - O(n + e(log(e)) + q(log(q)))
    # Space - O(n + q)
    #
    # where
    # n is the number of nodes
    # e is the number of edges
    # q is the number of queries
    #
    def distanceLimitedPathsExist(self, n: int, edge_list: List[List[int]], queries: List[List[int]]) -> List[bool]:
        def build_edge_list(edge_list):
            return sorted(edge_list, key=lambda x: x[2])

        uf = UnionFind(n)
        edge_list = build_edge_list(edge_list)
        output = [False] * len(queries)
        query_indices = defaultdict(list)
        for query_idx, (node_u, node_v, limit) in enumerate(queries):
            query_indices[(node_u, node_v, limit)].append(query_idx)
            
        edge_index = 0
        
        for node_u, node_v, limit_distance in sorted(queries, key=lambda x: x[2]):
            while edge_index < len(edge_list) and edge_list[edge_index][2] < limit_distance:
                uf.union(edge_list[edge_index][0], edge_list[edge_index][1])
                edge_index += 1
            output[query_indices[(node_u, node_v, limit_distance)].pop()] = uf.find(node_u) == uf.find(node_v)

        return output


# April 30, 2023

'''

# Kunal Wadhwa

'''