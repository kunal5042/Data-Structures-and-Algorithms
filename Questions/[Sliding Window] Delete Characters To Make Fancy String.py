# Question: https://leetcode.com/problems/delete-characters-to-make-fancy-string/
# Easy
# 
from typing import Optional, List

class Solution:
    # O(n) Time and O(1) Extra Space
    def makeFancyString(self, s: str) -> str:
        buffer = s[0]
        wstart = 0
        wend   = 1
        result = ''
        
        for idx in range(1, len(s)):
            if s[idx] == buffer:
                wend += 1
                
                if wend - wstart > 2:
                    wstart += 1
                    
            else:
                result += s[wstart : wend]
                wstart = idx
                wend   = idx + 1
                buffer = s[idx]
                
        
        result += s[wstart : wend]
        return result
'''

# Kunal Wadhwa

'''