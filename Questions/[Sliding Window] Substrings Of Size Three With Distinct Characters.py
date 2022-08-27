# Question: https://leetcode.com/problems/substrings-of-size-three-with-distinct-characters/
# Easy
from typing import Optional, List

class Solution:
    # O(n) Time and O(n) Space
    def countGoodSubstrings(self, s: str) -> int:
        if len(s) == 0: return 0
        
        good_substrings = 0
        last_seen = {s[0]: 0}
        window_start = 0
        
        for idx in range(1, len(s)):
            if s[idx] in last_seen and last_seen[s[idx]] >= window_start:
                window_start = last_seen[s[idx]] + 1
            
            if idx - window_start + 1 == 3:
                good_substrings += 1
                window_start += 1
                
            last_seen[s[idx]] = idx
            
        return good_substrings
'''

# Kunal Wadhwa

'''