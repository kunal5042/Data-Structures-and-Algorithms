# Question: https://leetcode.com/problems/minimum-fuel-cost-to-report-to-the-capital/
# Medium

import math
from collections import defaultdict
from typing import List

class Solution:
    # O(n) time and O(n) space
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        tree = defaultdict(set)
        
        for u, v in roads:
            tree[u].add(v)
            tree[v].add(u)
            
        visited = set()
        total_fuel = [0]
        
        # traverse down the tree
        # while backtracking, return the count of nodes in the subtree at each level
        # using this count compute the fuel cost from current node to it's parent
        def depth_first_search(node):
            visited.add(node)
            subtree = 1
            
            for adj in tree[node]:
                if adj not in visited:
                    node_count = depth_first_search(adj)
                    total_fuel[0] += math.ceil(node_count/seats)
                    subtree += node_count
                    
            return subtree
        
        depth_first_search(0)
        return total_fuel[0]
                
                


# February 12, 2023

'''

# Kunal Wadhwa

'''