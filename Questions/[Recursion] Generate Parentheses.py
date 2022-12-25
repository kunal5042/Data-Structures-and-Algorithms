# Question: https://leetcode.com/problems/generate-parentheses/
# Medium
from typing import Optional, List

class Solution:
    # written 5 months ago, Faster than 80%
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
        return result
    
    # written recently, Faster than 99%
    def generateParenthesis(self, n: int) -> List[str]:
        def generate(count_open, count_close, last_open, combination):
            if len(combination) == 2*n:
                combinations.append(combination)
                return
            
            if last_open is True:
                if count_open < n:
                    generate(count_open+1, count_close, True, combination+'(')
                if count_close + 1 <= count_open:
                    generate(count_open, count_close+1, False, combination+')')
                return
            
            if count_open < n:
                generate(count_open+1, count_close, True, combination+'(')
            if count_close + 1 <= count_open and count_close < n:
                generate(count_open, count_close+1, False, combination+')')
        
        combinations = []
        generate(0, 0, False, '')
        return combinations


# December 25, 2022

'''

# Kunal Wadhwa

'''