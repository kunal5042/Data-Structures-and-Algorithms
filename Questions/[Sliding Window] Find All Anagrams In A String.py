# Question: https://leetcode.com/problems/find-all-anagrams-in-a-string/

from typing import Optional, List

class Solution:
    # O(n) Time and O(n) Space
    def findAnagrams(self, s: str, p: str) -> List[int]:
        start_indices = []
        start, idx = None, 0
        _hash, can_permute = {}, {}
        
        # we need _hash contents to make an anagram of p
        for char in p: _hash[char] = _hash.get(char, 0) + 1
            
        while idx < len(s):
            if s[idx] in _hash:
                if start is None: start = idx
                can_permute[s[idx]] = can_permute.get(s[idx], 0) + 1
                
            else:
                can_permute = {}
                start = None
                
            if start is not None and (idx - start + 1) == len(p):
                if can_permute == _hash:
                    # can make an agram
                    # append the index of the start of this window
                    start_indices.append(start)
                    
                # we need to decrease window size
                # regardless of whether we can form an agram with current hashmap
                can_permute[s[start]] -= 1
                if can_permute[s[start]] == 0:
                    del can_permute[s[start]]
                        
                start += 1
                
            idx += 1
            
        return start_indices
'''

# Kunal Wadhwa

'''