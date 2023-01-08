# Question: https://leetcode.com/problems/most-profitable-path-in-a-tree/
# Medium
from typing import Optional, List

from collections import defaultdict
from functools import cache
class Solution:
    # O(n) time and O(n) space
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        graph = defaultdict(list)
        
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
            
        parents = {}
        visited = set()
        def fill_parents(node, parent):
            if node in visited: return
            visited.add(node)
            
            if node not in parents:
                parents[node] = parent
                
            for child in graph[node]:
                fill_parents(child, node)
            return
        fill_parents(0, -1)
        
        # bob traverses up to node 0
        path_bob = [bob]
        while path_bob[~0] != 0:
            path_bob.append(parents[path_bob[~0]])
            
        time_stamps = {node:time for time, node in enumerate(path_bob)}
        
        # alice 
        @cache
        def optimal_path(time, node, parent):
            bob_time = time_stamps.get(node, float('inf'))
            cost_or_reward = amount[node]
            
            if time == bob_time:
                cost_or_reward //= 2
            
            elif bob_time < time:
                cost_or_reward = 0
            
            children = [child for child in graph[node] if child != parent]
            if len(children) == 0:
                return cost_or_reward
                            
            most_optimal_income = mop = float('-inf')
            for child in children:
                mop = max(mop, cost_or_reward + optimal_path(time+1, child, node))
                
            return mop
        
        return optimal_path(0, 0, -1)


# January 08, 2023

'''

# Kunal Wadhwa

'''