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

    # solved again recently
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
    
'''

# Kunal Wadhwa

'''