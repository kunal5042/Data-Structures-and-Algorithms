# Question: https://leetcode.com/problems/partition-array-according-to-given-pivot/
# Medium
# 
from typing import Optional, List

class Solution:
    # O(n) Time and O(1) Space
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        result = [None for _ in range(len(nums))]
        smaller, greater = 0, len(nums)-1
        
        for idx in range(len(nums)):
            if nums[~idx] > pivot:
                result[greater] = nums[~idx]
                greater -= 1
                
            if nums[idx] < pivot:
                result[smaller] = nums[idx]
                smaller += 1
                
        while smaller <= greater:
            result[smaller] = pivot
            smaller += 1
            
        return result
        
    # O(n) Time and O(n) Space
    def _pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        smaller, greater = [], []
        pivots = []
        
        for idx in range(len(nums)):
            if nums[idx] < pivot:
                smaller.append(nums[idx])
                
            elif nums[idx] == pivot:
                pivots.append(pivot)
                
            else:
                greater.append(nums[idx])
                
        return smaller + pivots + greater
'''

# Kunal Wadhwa

'''