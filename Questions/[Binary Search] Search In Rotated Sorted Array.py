# Question: https://leetcode.com/problems/search-in-rotated-sorted-array/
# Medium
# To Do: Revisit
from typing import Optional, List

class Solution:
    # O(log(n)) Time and O(1) Space
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        
        while left <= right:
            m = middle = (left + right) // 2
            
            if nums[m] == target:
                return m
            
            if nums[left] <= nums[middle]:
                if all([target >= nums[left], target <= nums[middle]]):
                    right = middle - 1
                else:
                    left  = middle + 1
                    
            else:
                if all([target >= nums[middle], target <= nums[right]]):
                    left = middle + 1
                else:
                    right = middle - 1
                
        return -1
'''

# Kunal Wadhwa

'''
