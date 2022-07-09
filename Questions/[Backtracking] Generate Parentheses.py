# Question: https://leetcode.com/problems/generate-parentheses/

from typing import Optional, List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        def generate(combination, available, last_used, _open, _close):
            if available == 0:
                result.append(combination)
                return
            
            if _open <  n and len(combination) != (2*n)-1:
                generate(combination + '(', available-1, 'open', _open+1, _close)
                
            if _close < n and _open != 0 and _open - _close > 0:
                generate(combination + ')', available-1, 'close', _open, _close+1)            
            
            
        generate('', n*2, '', 0, 0)
        return sorted(result)
'''

# Kunal Wadhwa

'''