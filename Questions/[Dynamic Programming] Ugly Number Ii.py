# Question: https://leetcode.com/problems/ugly-number-ii/
# Medium

from typing import Optional, List

class Solution:
    def is_ugly(self, num):
        if num == 1: return True
        for divisor in [2,3,5]:
            while num % divisor == 0:
                num = num // divisor
        return num == 1
    
    # Brute Force Solution
    def nthUglyNumber_BRUTE_FORCE(self, n: int) -> int:
        ugly_count = 0
        num = 1
        while True:
            if self.is_ugly(num): ugly_count += 1
            if ugly_count == n: return num
            num += 1
        return
    
    # Optimal Solution
    # Using dynamic-programming 
    def nthUglyNumber(self, num: int) -> int:
        dp = [0 for _ in range(num)]
        dp[0] = 1
        iter2, iter3, iter5 = 0, 0, 0
        
        for idx in range(1, num):
            dp[idx] = min(dp[iter2]*2, dp[iter3]*3, dp[iter5]*5)
            if dp[idx] == dp[iter2]*2: iter2 += 1
            if dp[idx] == dp[iter3]*3: iter3 += 1                
            if dp[idx] == dp[iter5]*5: iter5 += 1
                
        return dp[~0]
'''

# Kunal Wadhwa

'''