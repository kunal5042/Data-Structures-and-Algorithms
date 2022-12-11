# Question: https://leetcode.com/problems/interleaving-string/
# Medium
from typing import Optional, List

class Solution:
    # O(n*m) Time and O(n*m) Space
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3): return False
        memo = {}
        def dfs(idx, jdx):
            if idx == len(s1) and jdx == len(s2): return True
            if (idx, jdx) in memo:
                return memo[(idx, jdx)]
            
            if idx < len(s1) and s3[idx+jdx] == s1[idx] and dfs(idx+1, jdx):
                memo[(idx, jdx)] = True
                return True
                
            if jdx < len(s2) and s3[idx+jdx] == s2[jdx] and dfs(idx, jdx+1):
                memo[(idx, jdx)] = True
                return True
            
            memo[(idx, jdx)] = False
            return False
        
        return dfs(0, 0)

'''

# Kunal Wadhwa

'''