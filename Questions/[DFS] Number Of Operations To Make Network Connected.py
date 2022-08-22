# Question: https://leetcode.com/problems/number-of-operations-to-make-network-connected/
# Medium
from typing import Optional, List

import random
from collections import defaultdict
class Solution:
    # O(V+E) Time and O(V) Space
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n - 1: return -1
        
        not_visited = set(range(n))
        visited = set()
        
        graph = defaultdict(set)
        for u, v in connections:
            graph[u].add(v)
            graph[v].add(u)
            
        def depth_first_search(node):
            if node in visited: return
            visited.add(node)
            not_visited.remove(node)
            
            for adj in graph[node]:
                depth_first_search(adj)

        
        result = -1
        # basically, keeping count of edges required to connect all the 
        # disconnected components of the graph
        while len(not_visited) != 0:
            result += 1
            
            random_node = not_visited.pop()
            not_visited.add(random_node)
            
            depth_first_search(random_node)
            
        return result
'''

# Kunal Wadhwa

'''