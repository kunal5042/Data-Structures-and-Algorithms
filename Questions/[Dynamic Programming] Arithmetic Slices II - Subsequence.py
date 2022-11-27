# Question: https://leetcode.com/problems/arithmetic-slices-ii-subsequence/
# Hard
from typing import Optional, List

class Solution:
    # O(n*n) time and o(n*n) space
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        output = 0
        dp = [defaultdict(int) for _ in range(len(nums))]
        
        for idx in range(1, len(nums)):
            for jdx in range(idx):
                delta = nums[idx] - nums[jdx]
                _sum = 0
                if delta in dp[jdx]:
                    _sum += dp[jdx][delta]
                    
                dp[idx][delta] += _sum + 1
                output += _sum
                
        return output


# November 27, 2022

'''

# Kunal Wadhwa

'''