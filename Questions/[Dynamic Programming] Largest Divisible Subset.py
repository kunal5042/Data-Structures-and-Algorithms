# Question: https://leetcode.com/problems/largest-divisible-subset/
# Medium
from typing import Optional, List

class Solution:
    # O(n*n) time and O(n) space
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        # every ith element in this array stores the size of the largest subset possible
        # with elements including and before this index
        x = [1 for idx in range(len(nums))]
        
        # this array stores the jth from which the ith index of array x is updated
        # more informally, it helps us construct the largest subset in efficient way
        # by storing information of the index of the factor of current multiple
        # where jth index is the factor and ith index is the multiple in the logic down below
        previous = [-1 for idx in range(len(nums))]
        
        # we ensure that the divisors are before the dividend
        # with the knowledge of below
        # if a divides b and b divides c: a divides c
        nums.sort()
        
        # stores the index of the last element of the largest subset
        largest_subset_idx = 0
        largest_subset = 1

        for idx in range(1, len(nums), 1):
            for jdx in range(idx-1, -1, -1):
                if nums[idx] % nums[jdx] == 0 and x[jdx] + 1 > x[idx]:
                    x[idx] = x[jdx] + 1
                    previous[idx] = jdx
                    
                    if x[idx] > largest_subset:
                        largest_subset = x[idx]
                        largest_subset_idx = idx
                    
        # construct the largest subset
        del largest_subset
        largest_subset = []
        build_idx = largest_subset_idx
        
        while build_idx >= 0:
            largest_subset.append(nums[build_idx])
            build_idx = previous[build_idx]
            
        return largest_subset
        


# January 01, 2023

'''

# Kunal Wadhwa

'''