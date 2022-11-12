# Question: https://leetcode.com/problems/string-to-integer-atoi/
# Medium
from typing import Optional, List

class Solution:
    def myAtoi(self, s: str) -> int:
        if len(s) == 0: return 0
        idx, sign, integer = 0, '+ve', []
        bounds = {'lower':-(2**31), 'upper':(2**31)-1}
        _map = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}
        
        while idx < len(s) and s[idx] == ' ':
            idx += 1
            
        if idx == len(s): return 0
        
        if s[idx] == '-':
            sign = '-ve'
            idx += 1
        
        elif s[idx] == '+':
            idx += 1
            
        if idx < len(s) and s[idx] not in _map: return 0
            
        while idx < len(s) and s[idx] not in _map:
            idx += 1
            
        if idx == len(s): return 0
            
        while idx < len(s) and s[idx] in _map:
            integer.append(_map[s[idx]])
            idx += 1
            
        output = 0
        for idx in range(len(integer)):
            output = ( (10**(len(integer)-idx-1)) * integer[idx] ) + output
            
        output *= -1 if sign == '-ve' else 1
            
        if output < bounds['lower']: return bounds['lower']
        if output > bounds['upper']: return bounds['upper']
        
        return output
'''

# Kunal Wadhwa

'''