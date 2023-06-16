# Question: https://leetcode.com/problems/number-of-ways-to-reorder-array-to-get-same-bst/description/
# Hard

import math
from typing import List

class Solution:
    def __init__(self):
        self.mod = (10**9) + 7

    def get_ways(self, nums):
        if len(nums) < 3:
            return 1

        left_nodes = []
        right_nodes = []

        for ele in nums:
            if ele < nums[0]: left_nodes.append(ele)
            if ele > nums[0]: right_nodes.append(ele)

        ways = self.get_ways(left_nodes)
        ways *= self.get_ways(right_nodes)
        ways *= math.comb(len(nums) - 1, len(left_nodes))
        ways %= self.mod
        return ways

    # O(n*n) time and O(n*n) space
    def numOfWays(self, nums: List[int]) -> int:
        return ( self.get_ways(nums) % self.mod ) - 1


# June 16, 2023

'''

# Kunal Wadhwa

'''