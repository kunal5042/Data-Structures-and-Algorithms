# Question: https://leetcode.com/problems/increasing-triplet-subsequence/
# Medium
from typing import Optional, List

import math
class Solution:
    # Brute optimized using extra space
    # O(n) Time and O(n) Space
    def increasingTriplet(self, nums: List[int]) -> bool:
        smallest = nums.copy()
        largest = nums.copy()
        
        jdx = len(nums)-2
        for idx in range(1, len(nums)):
            smallest[idx] = min(smallest[idx-1], nums[idx])
            largest[jdx] = max(largest[jdx+1], nums[jdx])
            jdx -= 1
            
        for idx in range(1, len(nums)-1):
            if nums[idx] > smallest[idx-1]:
                if nums[idx] < largest[idx+1]:
                    return True
                
        return False
    
    # Greedy space optimized
    # O(n) Time and O(1) Space
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 3: return False
        
        first = second = math.inf
        
        for ele in nums:
            if ele <= first:
                first = ele
            
            elif ele <= second:
                second = ele
                
            else:
                return True
            
        return False
'''

# Kunal Wadhwa

'''