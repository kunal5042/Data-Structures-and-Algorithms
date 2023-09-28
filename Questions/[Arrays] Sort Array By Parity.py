# Question: https://leetcode.com/problems/sort-array-by-parity/
# Easy

from typing import List

class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        # nums can be empty
        # nums can have all even
        # nums can have all odd
        
        # we can collect even and odd in two separate lists
        # and combine them later
        # time - O(n) space - O(n)
        
        # can we do better?
        # we are using two traversals in previous approach
        # can we make it one traversal?
        # we have to maintain the ordering of the elements
        # we can have a pointer to keep track of where even elements should go
        # as we traverse we can swap even elements with this pointer and increment it
        # that way as we traverse even elements are shifted to the front
        # and odd elements still maintain their order
        
        # apprach - 1
        result = []
        
        for ele in nums: 
            if ele % 2 == 0: result.append(ele)
                
        for ele in nums: 
            if ele % 2 != 0: result.append(ele)
                
        # apprach - 2
        even_ptr = 0
        for idx, ele in enumerate(nums):
            if nums[idx] % 2 == 0:
                nums[idx], nums[even_ptr] = \
                nums[even_ptr], nums[idx]
                even_ptr += 1
                
        return nums


# September 28, 2023

'''

# Kunal Wadhwa

'''