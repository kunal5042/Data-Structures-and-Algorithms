# Question: https://leetcode.com/problems/squares-of-a-sorted-array/
# Easy
# Square of a -ve number is +ve :)
from typing import Optional, List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        """Takes a sorted integer array nums.
        Returns a sorted array of squares of each element in nums
        """
        
        result = []
        lower, upper = 0, len(nums)-1
        
        # descending order insertion
        while lower <= upper:
            if abs(nums[lower]) > abs(nums[upper]):
                result.append(nums[lower]**2)
                lower += 1
            else:
                result.append(nums[upper]**2)
                upper -= 1
                
        result.reverse()
        return result
'''

# Kunal Wadhwa

'''