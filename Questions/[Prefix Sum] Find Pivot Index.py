# Question: https://leetcode.com/problems/find-pivot-index/
# Easy
from typing import Optional, List

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        _sum, total = 0, sum(nums)
        
        for idx in range(len(nums)):
            if (_sum * 2) + nums[idx] == total:
                return idx
            
            _sum += nums[idx]
            
        return -1
'''

# Kunal Wadhwa

'''