# Question: https://leetcode.com/problems/trapping-rain-water/
# Hard
from typing import Optional, List

class Solution:
    # O(n) Time and O(n) Space
    def trap(self, height: List[int]) -> int:
        if len(height) < 2: return 0
        
        # dynamic-programming
        # storing the left and right maximum height tower's height for every index
        left_max, right_max = [0] * len(height), [0] * len(height)
        left_max[0]   = height[0]
        right_max[~0] = height[~0]
        
        for idx in range(1, len(height)):
            left_max[idx]   = max(height[idx] , left_max[idx-1])
            right_max[~idx] = max(height[~idx], right_max[~(idx-1)])
            
        water = 0
        for idx in range(1, len(height)-1,):
            # using the previously stored information
            support_tower = min(left_max[idx], right_max[idx])
            
            # can't trap water
            if support_tower == 0: continue
            
            # update trapped water at current index
            water += (support_tower - height[idx])
            
        return water
'''

# Kunal Wadhwa

'''