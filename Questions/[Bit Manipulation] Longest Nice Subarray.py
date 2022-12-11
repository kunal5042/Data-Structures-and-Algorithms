# Question: https://leetcode.com/problems/longest-nice-subarray/
# Medium
from typing import Optional, List

class Solution:
    # O(n^2) Time and O(1) Space
    def longestNiceSubarray(self, nums: List[int]) -> int:
        nicest = 0
        
        for idx in range(len(nums)):
            length = 1
            signature = nums[idx]
            
            for jdx in range(idx+1, len(nums)):
                if signature & nums[jdx] == 0:
                    signature |= nums[jdx]
                    length += 1
                    continue
                    
                break
                
            nicest = max(nicest, length)
    
        return nicest
'''

# Kunal Wadhwa

'''