# Question: https://leetcode.com/problems/monotonic-array/
# Easy

from typing import List

class Solution:
    # O(n) time and O(1) space
    def isMonotonic(self, nums: List[int]) -> bool:
        # increasing
        # i < j nums[i] <= nums[j] 
        
        # decreasing
        # i < j nums[i] >= nums[j]
        
        # len(nums) could be 1
        
        increasing = True
        decreasing = True
        
        for idx in range(1, len(nums)):
            if nums[idx-1] > nums[idx]:
                increasing = False
                
            if nums[idx-1] < nums[idx]:
                decreasing = False
                
            if not increasing and not decreasing:
                return False
                
        return increasing or decreasing


# September 29, 2023

'''

# Kunal Wadhwa

'''