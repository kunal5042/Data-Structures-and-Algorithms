# Question: https://leetcode.com/problems/lexicographically-smallest-equivalent-string/
# Medium
from typing import Optional, List

class Solution:
    # O(n+m) time and O(n+m) space
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        graph = defaultdict(set)
        
        for idx in range(len(s1)):
            graph[s1[idx]].add(s2[idx])
            graph[s2[idx]].add(s1[idx])
            
        def get_char(node, visited):
            visited.add(node)
            char = node
            for neighbor in graph[node]:
                if neighbor not in visited:
                    char = min(char, get_char(neighbor, visited))
            return char
        
        replacement = {}
        result = ''
        for idx in range(len(baseStr)):
            if baseStr[idx] not in replacement:
                replacement[baseStr[idx]] = get_char(baseStr[idx], set())
            result += replacement[baseStr[idx]]
            
        return result



# January 14, 2023

'''

# Kunal Wadhwa

'''