# Question: https://leetcode.com/problems/flip-string-to-monotone-increasing/
# Medium
from typing import Optional, List

class Solution:
    # O(n) time and O(1) space
    def minFlipsMonoIncr(self, s: str) -> int:
        flips = Counter(s)['0']
        min_flips = flips
        
        for char in s:
            if char == '0':
                flips -= 1
            else:
                flips += 1
                
            min_flips = min(flips, min_flips)
            
        return min_flips


# January 17, 2023

'''

# Kunal Wadhwa

'''