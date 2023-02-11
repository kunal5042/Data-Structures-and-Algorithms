# Question: https://leetcode.com/problems/shortest-path-with-alternating-colors/
# Medium

import math
from collections import deque, defaultdict
from typing import List

class Solution:
    # O(n + e) time and O(n + e) space
    # where n is the number of nodes and e is the number of edges
    def shortestAlternatingPaths(self, n: int, red_edges: List[List[int]], blue_edges: List[List[int]]) -> List[int]:
        queue = deque([(0, 'R', 0), (0, 'B', 0)])
        distances = [math.inf for _ in range(n)]
        
        graph = defaultdict(set)
        for _from, _to in  red_edges: graph[_from].add((_to, 'R'))
        for _from, _to in blue_edges: graph[_from].add((_to, 'B'))
            
        visited = set()
        while len(queue) != 0:
            nodes_at_level = len(queue)
            
            for _ in range(nodes_at_level):
                node, prev, dist = queue.popleft()
                distances[node] = min(distances[node], dist)

                for adj, color in graph[node]:
                    # have we visited this node using an edge of this color
                    if (adj, color) in visited: continue
                        
                    # if colors are not alternating 
                    if color == prev: continue
                    queue.append((adj, color, dist+1))
                    
                visited.add((node, prev))
                
        return list(map(lambda x: -1 if x == math.inf else x, distances))
                


# February 11, 2023

'''

# Kunal Wadhwa

'''