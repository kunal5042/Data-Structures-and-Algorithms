# Question: https://leetcode.com/problems/number-of-ways-to-separate-numbers/
# Hard
from typing import Optional, List

class Solution:
    def numberOfCombinations(self, nums: str) -> int:
        lcs = [[0]*(len(nums)+1) for _ in range(len(nums))]
        for idx in reversed(range(len(nums))):
            for jdx in reversed(range(idx+1, len(nums))):
                if nums[idx] == nums[jdx]:
                    lcs[idx][jdx] = 1 + lcs[idx+1][jdx+1]
        
        def compare(idx, jdx, d): 
            m = lcs[idx][jdx]
            if m >= d: return True 
            return nums[idx+m] <= nums[jdx+m]

        dp = [[0]*(len(nums)+1) for _ in range(len(nums))]
        for idx in range(len(nums)): 
            if nums[idx] != "0": 
                for jdx in range(idx+1, len(nums)+1): 
                    if idx == 0:
                        dp[idx][jdx] = 1
                        continue
                        
                    dp[idx][jdx] = dp[idx][jdx-1]
                    if 2*idx-jdx >= 0 and compare(2*idx-jdx, idx, jdx-idx):
                        dp[idx][jdx] += dp[2*idx-jdx][idx]

                    if 2*idx-jdx+1 >= 0 and not compare(2*idx-jdx+1, idx, jdx-idx-1):
                        dp[idx][jdx] += dp[2*idx-jdx+1][idx]
                        
        return sum(dp[idx][len(nums)] for idx in range(len(nums))) % 1_000_000_007


# January 21, 2023

'''

# Kunal Wadhwa

'''