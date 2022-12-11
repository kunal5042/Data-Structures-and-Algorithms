# Question: https://leetcode.com/problems/climbing-stairs/
# Easy

class Solution:
    def climbStairs(self, n):
        if n < 3: return self.base(n)
            
        dp = [None for _ in range(n+1)]
        dp[0], dp[1], dp[2] = 0, 1, 2
        
        for idx in range(3, n+1):
            dp[idx] = dp[idx-1] + dp[idx-2]
            
        return dp[n]
    
    def base(self, n):
        dp = [0, 1, 2]
        return dp[n]
    
# Kunal Wadhwa
