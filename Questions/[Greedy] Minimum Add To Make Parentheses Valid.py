# Question: https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/
# Medium

from typing import Optional, List

class Solution:
    # O(n) Time and O(1) Space
    def minAddToMakeValid(self, s: str) -> int:
        open_required  = 0
        open_available = 0
        
        for char in s:
            if char == '(':
                open_available += 1
            else:
                if open_available == 0:
                    open_required += 1
                    
                else:
                    # greedily satisfy parantheses
                    open_available -= 1
                    
                    
        # for easier understanding
        close_required = open_available

        return open_required + close_required
'''

# Kunal Wadhwa

'''