# Question: https://leetcode.com/problems/majority-element/
# Easy
from typing import Optional, List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Moore's Voting Algorithm
        
        majority = nums[0]
        count = 1
        
        for idx in range(1, len(nums)):
            if nums[idx] == majority:
                count += 1
            else:
                count -= 1
                
            if count == 0:
                majority = nums[idx]
                count = 1
                    
        return majority
'''

# Kunal Wadhwa

'''