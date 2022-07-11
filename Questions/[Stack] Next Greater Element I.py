# Question: https://leetcode.com/problems/next-greater-element-i/

from typing import Optional, List

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """Takes two integer arrays
        Computes the next greater number in nums2 for every number in nums1
        Returns this result in a new list
        """
        stack = [nums2[~0]]
        empty = lambda x: len(x) == 0
        peek  = lambda x: x[~0]
        greater_map = {peek(stack): -1}
        
        # finding next greater for each element in nums2
        for idx in reversed(range(len(nums2)-1)):
            while not empty(stack) and peek(stack) < nums2[idx]:
                stack.pop()
            
            if empty(stack):
                greater_map[nums2[idx]] = -1
            else:
                greater_map[nums2[idx]] = peek(stack)
                
            stack.append(nums2[idx])
            
        # using previously computed next greater element to 
        # generate the resultant array
        return [greater_map[ele] for ele in nums1]

'''

# Kunal Wadhwa

'''