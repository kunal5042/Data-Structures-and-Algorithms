# Question: https://leetcode.com/problems/single-element-in-a-sorted-array/
# Medium
from typing import Optional, List

class Solution:
    # O(log(n)) time O(1) space
    def singleNonDuplicate(self, nums):
        low = 0
        high = len(nums)-1
        
        # binary search for the half which has uneven pairs
        while low < high:
            middle = low + (high-low)//2
            
            # even xor 1 = next odd      ; 4 ^ 1 = 5
            # odd  xor 1 = prev even     ; 5 ^ 1 = 4
            if nums[middle] == nums[middle ^ 1]:
                low = middle + 1
            else:
                high = middle
                
        return nums[low]


# November 22, 2022

'''

# Kunal Wadhwa

'''