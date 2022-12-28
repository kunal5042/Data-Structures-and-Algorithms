# Question: https://leetcode.com/problems/house-robber-ii/
# Medium
from typing import Optional, List

class Solution:
    # O(n) time and O(n) space
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2: return max(nums)
        
        path1 = [0 for _ in range(len(nums))]
        path2 = [0 for _ in range(len(nums))]
        path2[1] = nums[1]

        for idx in range(len(nums)):
            if idx >= 0 and idx < len(nums)-1:
                path1[idx+1] = max(path1[idx], path1[idx-1]+nums[idx])
                
            if idx >= 2 and idx <= len(nums)-1:
                path2[idx] = max(path2[idx-1], path2[idx-2]+nums[idx])
                
        return max(path1[~0], path2[~0])


# December 28, 2022

'''

# Kunal Wadhwa

'''