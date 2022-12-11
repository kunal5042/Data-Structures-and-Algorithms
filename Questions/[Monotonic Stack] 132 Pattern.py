# Question: https://leetcode.com/problems/132-pattern/
# Medium
from typing import Optional, List

import math
class Solution:
    # Brute-Force Solution
    # O(n^3) Time and O(1) Space
    def find132pattern(self, nums: List[int]) -> bool:
        if len(nums) < 3: return False
        
        for idx in range(len(nums)):
            for jdx in range(len(nums)-1):
                if nums[jdx] < nums[idx]: continue
                for kdx in reversed(range(jdx+1, len(nums))):
                    if nums[idx] < nums[kdx] and nums[kdx] < nums[jdx]:
                        return True
                    
        return False
    
    
    # O(n) Time and O(n) Space
    def find132pattern(self, nums: List[int]) -> bool:
        if len(nums) < 3: return False
        
        # monotonic-decreasing-stack
        stack = []
        
        for idx in range(len(nums)):
            if len(stack) == 0:
                stack.append([nums[idx], math.inf])
                continue
                
            current_ele_min = math.inf
            while len(stack) != 0 and nums[idx] >= stack[~0][0]:
                ele, ele_min = stack.pop()
                current_ele_min = min(ele, current_ele_min, ele_min)
                
            if len(stack) >= 1 and nums[idx] > stack[~0][1]: return True
            
            stack.append([nums[idx], current_ele_min])
            
        return False
'''

# Kunal Wadhwa

'''
