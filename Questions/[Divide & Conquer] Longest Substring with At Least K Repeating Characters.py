# Question: https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/solution/
# Medium
from typing import Optional, List

class Solution:
    # O(n^2) Time and O(n) Space
    def longestSubstring(self, s: str, k: int) -> int:
        STRING_LENGTH = len(s)
        result = 0
        
        # edge-case
        if k == 1:
            return STRING_LENGTH
        
        # edge-case
        if k > STRING_LENGTH:
            return 0
        
        def divide_and_conquer(left, right):
            nonlocal result
            
            # base-case
            if (right - left + 1) < k:
                return
            
            counts = {}
            # fill the map
            for idx in range(left, right+1):
                counts[s[idx]] = counts.get(s[idx], 0) + 1
                
            pointer = left
            
            for idx in range(left, right+1):
                # split array into two parts
                if counts[s[idx]] < k:
                    divide_and_conquer(left , idx-1)
                    divide_and_conquer(idx+1, right)
                    
                    # no point in proceeding further
                    break
                    
                pointer += 1
                
            # if pointer reached end, this substring is valid
            if pointer == right + 1:
                # update length
                result = max(result, right - left + 1)
                
            return
        
        divide_and_conquer(0, STRING_LENGTH-1)
        return result
'''

# Kunal Wadhwa

'''