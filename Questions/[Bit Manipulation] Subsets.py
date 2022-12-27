# Question: https://leetcode.com/problems/subsets/
# Medium
from typing import Optional, List

class Solution:
    # O(n * 2^n) time and O(n * 2^n) space
    # Based on Cascading Idea
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = [[]]
        
        for num in nums:
            level = []
            # from the previously generated subsets
            # generate new subsets by adding current num to them separately
            for generated_subsets in subsets:
                new_subset = generated_subsets + [num]
                level.append(new_subset)
                
            # adding new level after the loop so the size of iterator 
            # doesn't change as we traverse
            subsets += level
                
        return subsets
    
    # based on Backtracking
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = []
        
        def helper(idx, subset):
            if len(subset) == k:
                subsets.append(subset.copy())
                return
            
            for jdx in range(idx, len(nums)):
                subset.append(nums[jdx])
                helper(jdx+1, subset)
                subset.pop()
                
        for k in range(len(nums)+1):
            helper(0, [])
            
        return subsets
    
    # O(n * 2^n) time and O(n * 2^n) space
    # based on Lexicographic (Binary Sorted) Subsets
    # the idea is to map each subset to a bitmask of length n
    # where 1 on the ith position in bitmask means the presence of nums[i] in the subset
    # and 0 means its absence
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = []
        n = len(nums)
        for idx in range(2**n, 2**(n+1)):
            bitmask = bin(idx)[3:]
            subsets.append([nums[jdx] for jdx in range(n) if bitmask[jdx] == '1'])
            
        return subsets


# December 27, 2022

'''

# Kunal Wadhwa

'''