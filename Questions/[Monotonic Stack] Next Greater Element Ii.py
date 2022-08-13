# Question: https://leetcode.com/problems/next-greater-element-ii/

from typing import Optional, List

class Solution:
    # O(n) Time and O(n) Space
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        # for circular checking
        stack = nums[::-1]
        next_greater = [None] * len(nums)
        
        for idx in reversed(range(len(nums))):
            # maintaining a decreasing monotonic stack
            while len(stack) != 0 and nums[idx] >= stack[~0]:
                stack.pop()
                
            if len(stack) == 0:
                # if a greater element doesn't exit
                next_greater[idx] = -1
            else:
                next_greater[idx] = stack[~0]

            stack.append(nums[idx])
            
        return next_greater
'''

# Kunal Wadhwa

'''