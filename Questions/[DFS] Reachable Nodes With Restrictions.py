# Question: https://leetcode.com/problems/reachable-nodes-with-restrictions/
# Medium
# To Do: Solve using Union-Find ✅
from typing import Optional, List
from collections import defaultdict
class Solution:
    # O(V+E) Time and O(V) Space
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        restricted = set(restricted)
        graph   = defaultdict(set)
        visited = set()

        for node1, node2 in edges:
            # do not add an edge if any of the two nodes are in restricted
            if any([node1 in restricted, node2 in restricted]): continue
                
            graph[node1].add(node2)
            graph[node2].add(node1)

        def depth_first_search(node):
            result = 1

            for adjacent in graph[node]:
                if adjacent in visited: continue
                visited.add(adjacent)
                # update result
                result += depth_first_search(adjacent)

            return result

        visited.add(0)
        return depth_first_search(0)
'''

# Kunal Wadhwa

'''