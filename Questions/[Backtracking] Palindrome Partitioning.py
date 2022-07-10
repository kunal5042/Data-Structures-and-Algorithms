# Question: https://leetcode.com/problems/palindrome-partitioning/

from typing import Optional, List

class Solution:
    def is_palindrome(self, string, start, end):
        if start > end: return False
        while start <= end:
            if string[start] != string[end]:
                return False
            start += 1
            end   -= 1
        return True
    
    
    def partition(self, s: str) -> List[List[str]]:
        result = []
        
        def _partition(jdx, prev_part):
            if len(prev_part) == len(s) or jdx >= len(s):
                result.append(prev_part.copy())
                return
            
            for idx in range(jdx, len(s)):
                if self.is_palindrome(s, jdx, idx):
                    prev_part.append(s[jdx:idx+1])
                    _partition(idx+1, prev_part)
                    prev_part.pop()
                
        _partition(0, [])
        return result
'''

# Kunal Wadhwa

'''