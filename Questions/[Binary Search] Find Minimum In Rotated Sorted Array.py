# Question: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
# Medium
# To Do: Revisit
from typing import Optional, List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        """Takes a sorted(ascending) input array which is rotated between 1 and n times.
        Computes and returns the minimum element in this array in O(log(n)) time.
        Where n is the length of the input array
        """
        
        result = nums[0]
        left, right = 0, len(nums) - 1
        
        while left <= right:
            if nums[left] < nums[right]:
                result = min(nums[left], result)
                break
                
            
            middle = (left + right) // 2
            result = min(result, nums[middle])

            if nums[middle] >= nums[left]:
                left  = middle + 1
            else:
                right = middle - 1
                
        return result
'''

# Kunal Wadhwa

'''