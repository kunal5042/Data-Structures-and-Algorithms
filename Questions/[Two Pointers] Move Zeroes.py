# Question: https://leetcode.com/problems/move-zeroes/
# Easy
# 
from typing import Optional, List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        _put = 0
        for idx in range(len(nums)):
            this_num = nums[idx]
            
            if this_num != 0:
                nums[idx]  = 0
                nums[_put] = this_num
                _put += 1
                
        return
'''

# Kunal Wadhwa

'''