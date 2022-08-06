# Question: https://leetcode.com/problems/fibonacci-number/

from typing import Optional, List

class Solution:
    # simplest recursive implementation
    def fib(self, n: int) -> int:
        # base case
        if n == 0: return 0
        if n <= 2: return 1
        
        return self.fib(n-1) + self.fib(n-2)
    
    # dynamic-programming memoization
    def fib(self, n: int) -> int:
        memo = {}
        
        def helper(n):
            if n in memo: return memo[n]
            if n == 0   : return 0
            if n <= 2   : return 1
            
            memo[n] = helper(n-1) + helper(n-2)
            
            return memo[n]
        
        return helper(n)
    
    # dynamic-programming tabulation
    def fib(self, n: int) -> int:
        if n == 0: return 0
        if n <= 2: return 1
        
        tabulated = [None for _ in range(n+1)]
        tabulated[0], tabulated[1] = 0, 1
        
        for num in range(2, n+1):
            tabulated[num] = tabulated[num-1] + tabulated[num-2]
            
        return tabulated[~0]
'''

# Kunal Wadhwa

'''