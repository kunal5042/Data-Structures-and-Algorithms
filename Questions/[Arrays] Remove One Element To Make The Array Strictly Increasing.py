# Question: https://leetcode.com/problems/remove-one-element-to-make-the-array-strictly-increasing/

from typing import Optional, List

class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        if len(nums) <= 2: return True
        def is_decreasing(idx, upper_bound):
            for jdx in reversed(range(idx)):
                if nums[jdx] < upper_bound:
                    upper_bound = nums[jdx]
                    continue
                else:
                    return False
                
            return True

        
        def is_increasing(idx, lower_bound):
            for jdx in range(idx+1, len(nums)):
                if nums[jdx] > lower_bound:
                    lower_bound = nums[jdx]
                    continue
                else:
                    return False
                
            return True
        
        for kdx in range(len(nums)):
            if kdx == 0:
                if is_increasing(kdx, float('-inf')):
                    return True
                continue
                
            if kdx == len(nums)-1:
                if is_decreasing(kdx, float('inf')):
                    return True
                continue
                
            if is_increasing(kdx, nums[kdx-1]) and is_decreasing(kdx, nums[kdx+1]):
                return True
        
        return False	
'''

# Kunal Wadhwa


'''