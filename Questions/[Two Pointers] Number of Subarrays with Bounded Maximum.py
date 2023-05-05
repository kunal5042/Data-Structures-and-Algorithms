# Question: https://leetcode.com/problems/number-of-subarrays-with-bounded-maximum/
# Medium

from typing import List

class Solution:
    # O(n) time and O(1) space
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        result = 0
        start = -1
        end = -1
        
        for idx in range(len(nums)):
            if nums[idx] > right:
                start = end = idx
                continue
                
            if nums[idx] >= left:
                end = idx
                
            result += end - start
            
        return result
            
            
        


# May 05, 2023

'''

# Kunal Wadhwa

'''