# Question: https://leetcode.com/problems/splitting-a-string-into-descending-consecutive-values/
# Medium
from typing import Optional, List

class Solution:
    # O(n^n) Time and O(n) Space
    def splitString(self, s: str) -> bool:
        possible, splits = False, []
        
        def backtrack(jdx):
            nonlocal possible
            if possible is True:
                return
            
            if len(splits) >= 2:
                if splits[~1] - splits[~0] != 1:
                    return
                
            if jdx >= len(s) and len(splits) >= 2 and splits[~1] - splits[~0] == 1:
                possible = True
                return
                
            for idx in range(jdx, len(s)):
                splits.append(int(s[jdx:idx+1]))
                backtrack(idx+1)
                splits.pop()
                
        backtrack(0)
        return possible
'''

# Kunal Wadhwa

'''