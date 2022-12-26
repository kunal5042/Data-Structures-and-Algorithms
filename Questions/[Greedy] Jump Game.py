# Question: https://leetcode.com/problems/jump-game/
# Medium
from typing import Optional, List

class Solution:
    # Greedy
    # O(n) Time and O(1) Space
    def canJump(self, nums: List[int]) -> bool:
        # edge-case
        if len(nums) == 1: return True
        
        # edge-case
        if nums[0] == 0: return False
        
        max_reach = nums[0]
        
        for idx in range(1, len(nums)-1):
            if idx > max_reach: return False
            max_reach = max(idx + nums[idx], max_reach)
            
        return max_reach >= len(nums)-1

    # O(n) time and O(1) space
    # solved again recently as part of daily leetcode challenge
    def canJump(self, nums: List[int]) -> bool:
        max_reach = 0
        
        for idx in range(len(nums)):
            if idx > max_reach: return False
            if idx + nums[idx] > max_reach:
                max_reach = idx + nums[idx]
                
        return max_reach >= len(nums)-1
'''

# Kunal Wadhwa

'''