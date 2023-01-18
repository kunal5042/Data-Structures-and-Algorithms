# Question: https://leetcode.com/problems/maximum-sum-circular-subarray/
# Medium
from typing import Optional, List

class Solution:
    # O(n) time and O(1) space
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        min_subarray = current_min = float('inf')
        max_subarray = current_max = float('-inf')
        array_sum = 0
        
        for idx in range(len(nums)):
            current_min = min(current_min+nums[idx], nums[idx])
            min_subarray = min(current_min, min_subarray)
            
            current_max = max(current_max+nums[idx], nums[idx])
            max_subarray = max(current_max, max_subarray)
            
            array_sum += nums[idx]
            
        if max_subarray < 0:
            return max_subarray
        return max(max_subarray, array_sum - min_subarray)



# January 18, 2023

'''

# Kunal Wadhwa

'''