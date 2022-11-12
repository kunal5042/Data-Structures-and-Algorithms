# Question: https://leetcode.com/problems/house-robber-ii/
# Medium

from typing import Optional, List

class Solution:

    # O(n) Time and O(1) Space
    
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        
        def house_robber_one(nums, start, end):
            can_rob, can_not_rob = 0, 0
            
            for idx in range(start, end):
                temp = max(can_rob + nums[idx], can_not_rob)
                can_rob = can_not_rob
                can_not_rob = temp
                
            return max(can_rob, can_not_rob)
        
        return max(house_robber_one(nums, 0, len(nums)-1), 
                   house_robber_one(nums, 1, len(nums)))
    
'''

# Kunal Wadhwa

'''