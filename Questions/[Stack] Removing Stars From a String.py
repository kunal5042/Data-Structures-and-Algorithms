# Question: https://leetcode.com/problems/removing-stars-from-a-string/
# Medium
#
from typing import Optional, List

class Solution:
    # O(n) Time and O(n) Space
    def removeStars(self, s: str) -> str:
        if len(s) == 0: return s
        stack = []
        
        for char in s:
            if char == '*':
                stack.pop()
            else:
                stack.append(char)
                
        return ''.join(stack)
        
'''

# Kunal Wadhwa

'''