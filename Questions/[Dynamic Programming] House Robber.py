# Question: https://leetcode.com/problems/house-robber/
# Medium

from typing import Optional, List

class Solution:
    # O(n) time and O(1) space
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2: return max(nums)
        
        previous = 0
        current  = 0
        
        for idx in range(len(nums)):
            temp = current
            current  = max(previous + nums[idx], current)
            previous = temp
            
        return current
'''

# Kunal Wadhwa

'''
