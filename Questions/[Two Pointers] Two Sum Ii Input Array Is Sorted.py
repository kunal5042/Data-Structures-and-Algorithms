# Question: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
# Medium
# Classic!
from typing import Optional, List

class Solution:
    # O(n) Time and Constant Space
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """Finds the pair of two elements that sums upto target.
        Returns there indices in a list.
        Array is expected to be sorted and existence of one
        such pair is guaranteed.
        """
        
        left, right = 0, len(numbers)-1
        
        while left < right:
            potential = numbers[left] + numbers[right]

            if potential == target:
                return [left+1, right+1]
            
            if potential > target:
                right -= 1
            else:
                left  += 1
                
        raise Exception("Problem statement says there'll be atleast one solution")
'''

# Kunal Wadhwa

'''