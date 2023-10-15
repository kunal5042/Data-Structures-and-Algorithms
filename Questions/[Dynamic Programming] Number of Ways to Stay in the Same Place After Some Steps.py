# Question: https://leetcode.com/problems/number-of-ways-to-stay-in-the-same-place-after-some-steps/
# Hard

from functools import cache

class Solution:
    def __init__(self):
        self.ways = 0
        self.mod = (10**9) + 7
        self.allowed_steps = 0
        self.arr_length = 0
        
    def increment_ways(self, delta):
        self.ways += delta
        self.ways %= self.mod
       
    @cache
    def find_unique_ways(self, index, remaining_steps):
        if remaining_steps == 0:
            if index == 0:
                return 1
            return 0
        
        ways = 0
        
        # stay
        if remaining_steps - 1 >= index:
            ways += self.find_unique_ways(index, remaining_steps - 1)
            
        # move left
        if index - 1 >= 0 and remaining_steps >= index:
            ways += self.find_unique_ways(index-1, remaining_steps-1)
        
        # move right
        if index + 1 < self.arr_length and remaining_steps - 1 >= index + 1:
            ways += self.find_unique_ways(index+1, remaining_steps-1)
            
        return ways % self.mod
    
    def find_unique_ways_tabulated(self):
        dp = [[0 for _ in range(self.steps+1)] for _ in range(min(self.arr_length, self.steps))]
        dp[0][0] = 1
        
        for remaining_steps in range(1, self.steps + 1):
            for index in range(len(dp)-1, -1, -1):
                # stay
                ways = dp[index][remaining_steps-1]
                
                # move left
                if index > 0:
                    ways += dp[index-1][remaining_steps-1]
                    
                # move right
                if index < len(dp) - 1:
                    ways += dp[index+1][remaining_steps-1]
                    
                dp[index][remaining_steps] = ways
                
        return dp[0][self.steps] % self.mod
        
    def numWays(self, steps: int, arr_length: int) -> int:
        self.steps = steps
        self.arr_length = arr_length
        return self.find_unique_ways(0, self.steps)
        return self.find_unique_ways_tabulated()
    
        
        


# October 15, 2023

'''

# Kunal Wadhwa

'''