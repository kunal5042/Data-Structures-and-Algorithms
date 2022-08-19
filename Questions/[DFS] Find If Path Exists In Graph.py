# Question: https://leetcode.com/problems/find-if-path-exists-in-graph/

from typing import Optional, List

from collections import deque
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph   = {node_id: set() for node_id in range(n)}
        visited = set()
        
        for vertex1, vertex2 in edges:
            graph[vertex1].add(vertex2)
            graph[vertex2].add(vertex1)
            
        def depth_first_search(node_id):
            if node_id in visited: return False
            if node_id == destination: return True
            
            visited.add(node_id)
            
            for adjacent in graph[node_id]:
                if depth_first_search(adjacent) is True:
                    return True
                
            return False
        
        return depth_first_search(source)
'''

# Kunal Wadhwa

'''