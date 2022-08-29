# Question: https://leetcode.com/problems/powx-n/
# Medium
from typing import Optional, List

class Solution:
    # O(log(n)) Time
    def myPow(self, x: float, n: int) -> float:
        memo = {}
        
        def pow(n):
            if n == 0: return 1
            if n == 1: return x
            if n in memo: return memo[n]
            
            if n % 2 == 0:
                memo[n] = pow(n//2) * pow(n//2)
                return memo[n]
            else:
                memo[n] = pow(n//2) * pow(n//2) * x
                return memo[n]
            
        return pow(n) if n >= 0 else 1/pow(abs(n))
'''

# Kunal Wadhwa

'''