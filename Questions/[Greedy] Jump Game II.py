# Question: https://leetcode.com/problems/jump-game-ii/
# Medium

from functools import cache
from typing import List

class Solution:
    # O(n) time and O(max(nums[i] + j)) space
    def jump(self, nums: List[int]) -> int:
        nums = [nums[idx] + idx for idx in range(len(nums))]

        start = 0
        reach = nums[0]
        steps = 1
        
        while reach < len(nums)-1:
            steps += 1
            cache = reach
            reach = max(
                [nums[idx] for idx in range(start, reach+1)]
            )
            start = cache
            
        return steps if len(nums) > 1 else 0


# February 08, 2023

'''

# Kunal Wadhwa

'''