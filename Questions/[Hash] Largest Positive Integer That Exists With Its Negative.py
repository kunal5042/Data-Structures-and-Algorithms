# Question: https://leetcode.com/problems/largest-positive-integer-that-exists-with-its-negative/description/
# Easy

from typing import List

class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        _hash = set()
        res = -1

        for ele in nums:
            mod_ele = abs(ele)

            if mod_ele > res and -ele in _hash:
                res = mod_ele

            _hash.add(ele)

        return res


# May 02, 2024

'''

# Kunal Wadhwa

'''