# Question: https://leetcode.com/problems/subsets/

from typing import Optional, List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """Takes an integer array.
        Returns the powerset of the given array
        """
        
        subsets = []
        
        def helper(current, jdx):
            if jdx > len(nums): return
            subsets.append(current.copy())
            
            for idx in range(jdx, len(nums)):
                current.append(nums[idx])
                helper(current, idx+1)
                current.pop()
                
            return subsets
        
        return helper([], 0)
'''

# Kunal Wadhwa

'''