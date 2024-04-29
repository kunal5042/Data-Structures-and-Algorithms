# Question: https://leetcode.com/problems/minimum-number-of-operations-to-make-array-xor-equal-to-k/description/?envType=daily-question&envId=2024-04-29
# Medium

from typing import List

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        xor_nums = k
        for ele in nums:
            xor_nums ^= ele

        return bin(xor_nums).count('1')


# April 29, 2024

'''

# Kunal Wadhwa

'''