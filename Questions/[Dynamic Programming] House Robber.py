# Question: https://leetcode.com/problems/house-robber/

from typing import Optional, List

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        
        first, second = 0, 0
        
        for idx in range(len(nums)):
            temp   = second
            second = max(first, second, first + nums[idx])
            first  = temp
        
        return max(first, second)
'''

# Kunal Wadhwa

'''