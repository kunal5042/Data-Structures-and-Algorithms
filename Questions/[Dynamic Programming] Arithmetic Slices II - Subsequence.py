# Question: https://leetcode.com/problems/arithmetic-slices-ii-subsequence/
# Hard
from typing import Optional, List
from collections import defaultdict

class Solution:
    # O(n*n) time and o(n*n) space
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        arith_subseqs = 0
        dp = [defaultdict(int) for _ in range(len(nums))]
        
        for idx in range(1, len(nums)):
            for jdx in range(idx):
                difference = nums[idx] - nums[jdx]
                _sum = 0
                if difference in dp[jdx]:
                    _sum += dp[jdx][difference]
                    
                dp[idx][difference] += _sum + 1
                arith_subseqs += _sum
                
        return arith_subseqs


# November 27, 2022

'''

# Kunal Wadhwa

'''