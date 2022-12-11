# Question: https://leetcode.com/problems/detect-capital/
# Easy
# 
from typing import Optional, List
import string
class Solution:
    # O(n) Time and O(1) Space
    def detectCapitalUse(self, word: str) -> bool:
        small   = set(string.ascii_lowercase)
        capital = set(string.ascii_uppercase)
        
        all_small   = True
        all_capital = True
        
        for idx in range(1, len(word)):
            if word[idx] in capital:
                all_small  = False
            else:
                all_capital = False
                
        
        return any([word[0] in capital and all_capital,
                    word[0] in capital and all_small,
                    word[0] in small   and all_small])
    
    
'''

# Kunal Wadhwa

'''