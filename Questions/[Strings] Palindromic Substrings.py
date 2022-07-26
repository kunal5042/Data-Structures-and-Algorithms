# Question: https://leetcode.com/problems/palindromic-substrings/

from typing import Optional, List

class Solution:
    def countSubstrings(self, s: str) -> int:
        if len(s) == 1: return 1
        
        def valid(left, right):
            if any([left < 0, right >= len(s)]):
                return False
            return True
        
        count = 1
        for idx in range(1, len(s)):
            count += 1
            
            # odd
            left, right = idx - 1, idx + 1
            while valid(left, right) and s[left] == s[right]:
                left  -= 1
                right += 1
                count += 1
                
            # even
            left, right = idx - 1, idx
            while valid(left, right) and s[left] == s[right]:
                left -= 1
                right += 1
                count += 1
        
        return count
'''

# Kunal Wadhwa

'''