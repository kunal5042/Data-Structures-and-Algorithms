# Question: https://leetcode.com/problems/arithmetic-subarrays/description/
# Medium

from typing import List

class Solution:
    def isAirthmetic(self, array):
        if len(array) < 2: return False
        delta = array[1] - array[0]
        for idx in range(2, len(array)):
            if array[idx] - array[idx-1] != delta:
                return False
        return True

    def checkArithmeticSubarrays(self, nums: List[int], lbound: List[int], rbound: List[int]) -> List[bool]:
        result = []

        for idx in range(len(lbound)):
            left = lbound[idx]
            right = rbound[idx]
            subarray = sorted(nums[left:right+1])
            result.append(self.isAirthmetic(subarray))

        return result


# November 23, 2023

'''

# Kunal Wadhwa

'''