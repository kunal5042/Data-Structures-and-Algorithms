# Question: https://leetcode.com/problems/check-if-all-as-appears-before-all-bs/
# Easy
#
from typing import Optional, List

class Solution:
    # O(n) Time and O(1) Space
    def checkString(self, s: str) -> bool:
        a_present, last_a  = False, float('-inf')
        b_present, first_b = False, float('inf')
        
        for idx in range(len(s)):
            if s[idx] == 'a':
                a_present = True
                last_a = idx
                continue
                
            if b_present is False:
                b_present = True
                first_b = idx
                
            if last_a > first_b: return False
            
        return last_a < first_b
'''

# Kunal Wadhwa

'''