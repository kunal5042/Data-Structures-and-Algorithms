# Question: https://leetcode.com/problems/rotate-function/
# Medium
from typing import Optional, List

class Solution:
    # rotation function can be generalized as 
    # F(k) = F(k-1) + sum(arr) - len(arr)*arr[len(arr) - k]
    # we can use an array to values of previous rotation functions
    # but, we only need the immediate previous value
    # hence we can suffice with just one variable
    #
    # O(n) time and O(1) space
    def maxRotateFunction(self, nums: List[int]) -> int:
        _sum = sum(nums)
        previous = result = sum([idx*ele for idx, ele in enumerate(nums)])
        
        for k in range(1, len(nums)):
            rotation_function_of_k = previous + _sum - len(nums)*nums[len(nums)-k]
            result = max(result, rotation_function_of_k)
            previous = rotation_function_of_k
            
        return result


# January 01, 2023

'''

# Kunal Wadhwa

'''