# Question: https://leetcode.com/problems/find-peak-element/
# Medium
'''
O(log(n)) using Binary Search

How this works ->
4 Cases for middle element:
    - (middle smaller than previous and smaller than next) (Peak can be found in any direction)
    - (middle smaller than previous and greater than next) (Peak in left direction)
    - (middle greater than previous and smaller than next) (Peak in right direction)
    - (middle greater than previous and greater than next) (Peak)
    
    
BASE: We are guaranteed to find peak in the direction where middle is smaller than the first element in that direction
Because, if we move further in that direction either the next elements in that direction will keep increasing in which we will reach either the end or the start which will be our peaks.
As given nums[-1] and nums[n] = -inf
Or, one of the next elements in that direction will be smaller, making the previous element the peak.

Hence, we can apply the following logic
'''
from typing import List, Optional
class Solution:
    # O(log(n)) Time and O(1) Space
    # Cleaner
    def findPeakElement(self, nums):
        left, right = 0, len(nums)-1
        
        while left < right:
            middle = (left + right) // 2
            
            if nums[middle] < nums[middle+1]:
                left = middle + 1
            else:
                right = middle 
                
        return left
    
    
    # Easy to understand
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        
        left, right = 0, len(nums)-1
        
        while left <= right:
            middle = (left + right) // 2
            
            if middle == 0:
                if nums[middle] > nums[middle+1]:
                    return middle
                
            if middle == len(nums)-1:
                if nums[middle] > nums[middle-1]:
                    return middle
                
            if nums[middle] > nums[middle-1] and nums[middle] > nums[middle+1]:
                return middle
            
        
            if nums[middle] < nums[middle+1]:
                left  = middle + 1
                
            else: 
                right = middle - 1
                
# Kunal Wadhwa
        
