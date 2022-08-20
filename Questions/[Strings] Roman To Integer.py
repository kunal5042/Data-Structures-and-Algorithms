# Question: https://leetcode.com/problems/roman-to-integer/
# Easy
# 
from typing import Optional, List

class Solution:
    # O(n) Time and O(1) Space
    def romanToInt(self, s: str) -> int:
        hash_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        
        integer = 0
        idx = len(s) - 1
        
        while idx > -1:
            if any([s[idx] == 'V', s[idx] == 'X']):
                if idx - 1 > -1 and s[idx-1] == 'I':
                    integer += hash_map[s[idx]] - hash_map[s[idx-1]]
                    idx = idx - 1
                else:
                    integer += hash_map[s[idx]]
                    
            elif any([s[idx] == 'L', s[idx] == 'C']):
                if idx - 1 > -1 and s[idx-1] == 'X':
                    integer += hash_map[s[idx]] - hash_map[s[idx-1]]
                    idx = idx - 1
                else:
                    integer += hash_map[s[idx]]
                    
                
            elif any([s[idx] == 'D', s[idx] == 'M']):
                if idx - 1 > -1 and s[idx-1] == 'C':
                    integer += hash_map[s[idx]] - hash_map[s[idx-1]]
                    idx = idx - 1
                else:
                    integer += hash_map[s[idx]]
                    
            else:
                integer += hash_map[s[idx]]
                
                
            idx -= 1
            
        return integer	
'''

# Kunal Wadhwa

'''