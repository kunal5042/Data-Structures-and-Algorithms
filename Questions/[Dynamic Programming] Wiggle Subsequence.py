# Question: https://leetcode.com/problems/wiggle-subsequence/
# Medium

from typing import Optional, List

class Solution:
    # O(n) Time and O(n) Space
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if len(nums) < 2: return len(nums)
        
        # Using Dynamic-Programming
        # At every index we will store the length of the wiggle subsequence
        # ending at the current index
        
        # up_wiggle will store the length of the wiggle subsequence
        # ending at an up wiggle
        
        # similarly down_wiggle will store the length of the wiggle subsequence
        # ending at a down wiggle
        up_wiggle   = [0 for _ in range(len(nums))]
        down_wiggle = [0 for _ in range(len(nums))]

        up_wiggle[0], down_wiggle[0] = 1, 1
        
        for idx in range(1, len(nums)):
            # going up_wiggle
            if nums[idx] > nums[idx-1]:
                up_wiggle[idx]   = down_wiggle[idx-1] + 1
                # no increment in down wiggle sequence
                down_wiggle[idx] = down_wiggle[idx-1]
                
            # coming down_wiggle
            elif nums[idx] < nums[idx-1]:
                down_wiggle[idx] = up_wiggle[idx-1] + 1
                up_wiggle[idx]   = up_wiggle[idx-1]
                
            else:
                # can't wiggle
                down_wiggle[idx] = down_wiggle[idx-1]
                up_wiggle[idx]   = up_wiggle[idx-1]
                
        return max(down_wiggle[~0], up_wiggle[~0])
'''

# Kunal Wadhwa

'''