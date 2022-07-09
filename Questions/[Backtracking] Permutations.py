# Question: https://leetcode.com/problems/permutations/

from typing import Optional, List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not len(nums)  : return [[]]
        if len(nums) == 1 : return [nums]
        
        result = []
        def permute(permutation, choices):
            if len(choices) == 0:
                result.append(permutation)
                
            for idx, _choice in enumerate(choices):
                permute(permutation + [_choice], choices[:idx] + choices[idx+1:])
                
        permute([], nums)
        return result
        
'''

# Kunal Wadhwa

'''