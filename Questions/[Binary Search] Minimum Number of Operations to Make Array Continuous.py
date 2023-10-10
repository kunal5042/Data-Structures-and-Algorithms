# Question: https://leetcode.com/problems/minimum-number-of-operations-to-make-array-continuous/
# Hard

import bisect
from typing import List

class Solution:
    # O(n * log(n)) time and O(1) space
    def minOperations(self, nums: List[int]) -> int:
        result = len(nums)
        array  = sorted(set(nums))
        
        for idx in range(len(array)):
            left = array[idx]
            right = left + len(nums) - 1
            end = bisect.bisect_right(array, right)
            present = end - idx
            result = min(result, len(nums) - present)
            
        return result


# October 10, 2023

'''

# Kunal Wadhwa

'''