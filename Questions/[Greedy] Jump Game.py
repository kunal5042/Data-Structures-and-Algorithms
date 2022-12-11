# Question: https://leetcode.com/problems/jump-game/
# Medium
from typing import Optional, List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        can_reach = [False for _ in range(len(nums))]
        can_reach[0] = True
        
        for idx in range(len(can_reach)):
            if can_reach[idx] is True:
                max_jump = nums[idx]
                
                for offset in range(1, max_jump+1):
                    if idx + offset >= len(nums)  : break
                    if idx + offset == len(nums)-1: return True
                    can_reach[idx+offset] = True
                    
        
        return can_reach[~0]
    
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
'''

# Kunal Wadhwa

'''