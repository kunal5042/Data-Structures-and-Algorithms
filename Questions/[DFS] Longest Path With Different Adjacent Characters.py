# Question: https://leetcode.com/problems/longest-path-with-different-adjacent-characters/
# Hard
from typing import Optional, List

class Solution:
    # O(n) time and O(n) space
    def longestPath(self, parent: List[int], s: str) -> int:
        graph = defaultdict(set)
        graph[0] = set()
        
        for idx in range(1, len(parent)):
            graph[parent[idx]].add(idx)
            graph[idx].add(parent[idx])
        
        visited = set()
        longest = float('-inf')
        
        def depth_first(node, parent):
            nonlocal longest
            chains = [0]
            for neighbor in graph[node]:
                if neighbor != parent:
                    chains.append(depth_first(neighbor, node))
                    
            chains.sort(reverse=True)
            longest = max(longest, 1 + sum(chains[:2]))
            if s[node] != s[parent]:
                return 1 + max(chains[:2])
            return 0            
            
        depth_first(0, -1)
        return longest if longest != float(-inf) else 1


# January 13, 2023

'''

# Kunal Wadhwa

'''