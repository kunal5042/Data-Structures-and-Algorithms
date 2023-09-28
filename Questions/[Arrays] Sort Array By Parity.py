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
        # any how we will need two traversals
        
        result = []
        
        for ele in nums: 
            if ele % 2 == 0: result.append(ele)
                
        for ele in nums: 
            if ele % 2 != 0: result.append(ele)
                
        return result


# September 28, 2023

'''

# Kunal Wadhwa

'''