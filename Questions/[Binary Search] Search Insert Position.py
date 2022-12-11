# Question: https://leetcode.com/problems/search-insert-position/
# Easy
from typing import Optional, List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        """Takes a sorted integer array of distinct values nums.
        And an integer target.
        Finds the index in which target can be inserted so that 
        the array remains sorted
        """
        left, right = 0, len(nums)-1
        
        while left <= right:
            middle = (left + right) // 2
            
            if nums[middle] == target:
                return middle
            
            if nums[middle] > target:
                right = middle - 1
                
            else:
                left = middle + 1
                
        return left

'''

# Kunal Wadhwa

'''