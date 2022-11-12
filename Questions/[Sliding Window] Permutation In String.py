# Question: https://leetcode.com/problems/permutation-in-string/
# Medium

from typing import Optional, List

class Solution:
    # O(n) Time and O(n) Space
    def checkInclusion(self, s1: str, s2: str) -> bool:
        _hash = {}
        for char in s1: _hash[char] = _hash.get(char, 0) + 1
        
        start, idx = None, 0
        can_permute = {}
        
        while idx < len(s2):
            if s2[idx] in _hash:
                if start is None: start = idx
                can_permute[s2[idx]] = can_permute.get(s2[idx], 0) + 1
                
            else:
                # faster than dict.clear()
                can_permute = {}
                start = None
                
            # window size is same
            # does this window qualify for a permutation of s1
            if start is not None and idx - start + 1 == len(s1):
                if can_permute == _hash: return True
                
                # remove left-most
                # decrease window size
                can_permute[s2[start]] -= 1
                if can_permute[s2[start]] == 0:
                    del can_permute[s2[start]]
                    
                # udpate start of the window
                start += 1
                
            idx += 1
                    
        return False
'''

# Kunal Wadhwa

'''