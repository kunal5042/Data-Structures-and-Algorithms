# Question: https://leetcode.com/problems/magical-string/
# Medium
from typing import Optional, List

class Solution:
    def magicalString(self, n: int) -> int:
        magic = [1, 2, 2]
        idx = 2
        
        while len(magic) < n:
            magic += magic[idx] * [3 - magic[~0]]
            idx += 1
            
        return magic[:n].count(1)


# January 12, 2023

'''

# Kunal Wadhwa

'''