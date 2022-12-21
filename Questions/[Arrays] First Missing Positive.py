# Question: https://leetcode.com/problems/first-missing-positive/
# Hard
from typing import Optional, List

class Solution:
    # O(n) time and O(1) space
    def firstMissingPositive(self, nums: List[int]) -> int:
        for idx in range(len(nums)):
            if nums[idx] <= 0: nums[idx] = float('inf')
                
        for idx in range(len(nums)):
            if nums[idx] == float('inf'): continue
            index = abs(nums[idx]) - 1
            if index < 0 or index >= len(nums) or nums[index] < 0: continue
            nums[index] *= -1
            
        for idx in range(len(nums)):
            if nums[idx] >= 0:
                return idx + 1
            
        return len(nums)+1


# December 21, 2022

'''

# Kunal Wadhwa

'''