# Question: https://leetcode.com/problems/minimum-time-to-collect-all-apples-in-a-tree/
# Medium
from typing import Optional, List

class Solution:
    # O(n) time and O(n) space
    def minTime(self, n: int, edges: List[List[int]], has_apple: List[bool]) -> int:
        graph = defaultdict(set)
        for node_u, node_v in edges:
            graph[node_u].add(node_v)
            graph[node_v].add(node_u)
        
        def depth_first_search(node):
            if node in visited: return False
            visited.add(node)
            for neighbor in graph[node]:
                if depth_first_search(neighbor) is True:
                    has_apple[node] = True
            return has_apple[node]
        
        visited = set()
        depth_first_search(0)
        time = (sum(has_apple)-1) * 2
        return time if time > 0 else 0


# January 11, 2023

'''

# Kunal Wadhwa

'''