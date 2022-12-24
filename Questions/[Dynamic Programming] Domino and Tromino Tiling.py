# Question: https://leetcode.com/problems/domino-and-tromino-tiling/
# Medium
from typing import Optional, List

class Solution:
    cache_dom = {0:1, 1:1, 2:2}
    cache_trom = {0:0, 1:0, 2:1}
    
    def numTilings(self, n: int) -> int:
        mod = 10**9 + 7
        
        def domino(num):
            if num in Solution.cache_dom:
                return Solution.cache_dom[num]
            
            Solution.cache_dom[num] = (domino(num-1) + domino(num-2) + 2 * tromino(num-1)) % mod
            return Solution.cache_dom[num]
        
        def tromino(num):
            if num in Solution.cache_trom:
                return Solution.cache_trom[num]
            
            Solution.cache_trom[num] = (domino(num-2) + tromino(num-1)) % mod
            return Solution.cache_trom[num]
        
        return domino(n)


# December 24, 2022

'''

# Kunal Wadhwa

'''