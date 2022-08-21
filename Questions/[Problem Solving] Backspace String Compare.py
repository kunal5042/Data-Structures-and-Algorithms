# Question: https://leetcode.com/problems/backspace-string-compare/
# Easy
from typing import Optional, List

class Solution:
    # O(max(len(s), len(t))) Time and Same Space
    def backspaceCompare(self, s: str, t: str) -> bool:
        def get_final_string(s):
            stack = []
        
            for idx in range(len(s)):
                if s[idx] == '#' and len(stack) != 0:
                    stack.pop()

                if s[idx] != '#':
                    stack.append(s[idx])
                
            return "".join(stack)
        
        return get_final_string(s) == get_final_string(t)
'''

# Kunal Wadhwa

'''