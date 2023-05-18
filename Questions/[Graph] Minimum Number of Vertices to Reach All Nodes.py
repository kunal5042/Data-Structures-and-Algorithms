# Question: https://leetcode.com/problems/minimum-number-of-vertices-to-reach-all-nodes/
# Medium

from typing import List

class Solution:
    # O(e+v) time and O(v) space
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        not_reachable = set([ele for ele in range(n)])
        
        for _from, _to in edges:
            not_reachable.discard(_to)
        
        return list(not_reachable)


# May 18, 2023

'''

# Kunal Wadhwa

'''