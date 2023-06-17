# Question: https://leetcode.com/problems/make-array-strictly-increasing/description/
# Hard

import bisect, math
from functools import cache
from typing import List

class Solution:
    def __init__(self):
        self.arr1 = None
        self.arr2 = None

    @cache
    def get_minimum_operations(self, idx, prev):
        if idx == len(self.arr1):
            return 0

        operations = math.inf

        if self.arr1[idx] > prev:
            operations = self.get_minimum_operations(idx + 1, self.arr1[idx])

        replacement_idx = bisect.bisect_right(self.arr2, prev)

        if replacement_idx < len(self.arr2):
            operations = min(operations, 1 + self.get_minimum_operations(idx + 1, self.arr2[replacement_idx]))

        return operations

    # m = len(arr1)
    # n = len(arr2)
    #
    # O(m * n * log(n)) time and O(m * n) space
    #
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        arr2.sort()
        self.arr1 = arr1
        self.arr2 = arr2
        result = self.get_minimum_operations(0, -1)
        return result if result != math.inf else -1


# June 17, 2023

'''

# Kunal Wadhwa

'''