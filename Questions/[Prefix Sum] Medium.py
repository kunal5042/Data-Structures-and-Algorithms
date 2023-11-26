# Question: https://leetcode.com/problems/sum-of-absolute-differences-in-a-sorted-array/description/
# Sum Of Absolute Differences

from typing import List

class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        left_p  = [x for x in nums]
        right_p = [x for x in nums]
        result  = [0 for x in nums]

        for idx in range(1, len(nums)-1):
            left_p[idx] = left_p[idx-1] + nums[idx]
            right_p[~idx] = right_p[~(idx-1)] + nums[~idx]

        left_p[~0] = left_p[~1] + nums[~0]
        right_p[0] = right_p[1] + nums[0]

        for idx in range(0, len(nums)):
            rcount = len(nums) - idx
            lcount = idx + 1

            delta_right = abs(right_p[idx] - (nums[idx]*rcount))
            delta_left = abs(left_p[idx] - (nums[idx]*lcount))

            result[idx] = delta_left + delta_right

        return result



# November 26, 2023

'''

# Kunal Wadhwa

'''