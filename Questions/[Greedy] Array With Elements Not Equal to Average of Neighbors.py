# Question: https://leetcode.com/problems/array-with-elements-not-equal-to-average-of-neighbors/
# Medium
from typing import Optional, List

class Solution:
    # O(n * log(n)) Time and O(n) Space
    
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        # Logic
        # sort the input array
        # take first half and insert them in space separated fashion
        # take the second half, insert them in spaces starting from 1 
        # what this does is, we are guaranteeing that either both the neighbors will be larger than middle
        # or both smaller than middle
        # and for neighbors / 2 to be equal to middle; one neighbor must be larger and one must be smaller
        # sorting guarantees that the second half elements will be larger than first half
        # hence, we can safely insert them
        
        result = [None for _ in range(len(nums))]
        nums.sort()
        
        jdx = 0
        for idx in range(0, len(nums), 2):
            result[idx] = nums[jdx]
            jdx += 1
            
        
        jdx = len(nums) // 2 + 1 if len(nums) % 2 != 0 else len(nums) // 2
        for idx in range(1, len(nums), 2):
            result[idx] = nums[jdx]
            jdx += 1
            
            
        return result
'''

# Kunal Wadhwa

'''