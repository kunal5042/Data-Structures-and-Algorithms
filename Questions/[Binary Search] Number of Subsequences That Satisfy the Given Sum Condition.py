# Question: https://leetcode.com/problems/number-of-subsequences-that-satisfy-the-given-sum-condition/
# Medium

import bisect
from typing import List

class Solution:
    # O(n*log(n)) time and O(1) space
    def numSubseq(self, nums: List[int], target: int) -> int:
        result = 0
        mod = 10**9 + 7
        nums.sort()
        
        for left in range(len(nums)):
            right = bisect.bisect_right(nums, target - nums[left]) - 1
            if right >= left:
                result += 2**(right-left)
                result %= mod
                
        return int(result)


# May 06, 2023

'''

# Kunal Wadhwa

'''