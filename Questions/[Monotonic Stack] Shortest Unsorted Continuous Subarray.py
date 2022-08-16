# Question: https://leetcode.com/problems/shortest-unsorted-continuous-subarray/

from typing import Optional, List

class Solution:
    # O(n) Time and O(n) Space
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        result = 0
        
        # monotonic-increasing-stack
        stack = []
        
        sub_start, sub_end = float('inf'), float('-inf')
        
        for idx in range(len(nums)):
            # stack-empty
            if len(stack) == 0:
                stack.append([nums[idx], idx])
                continue
                
            # saving top of stack
            cur_top, cur_top_idx = stack[~0]
            
            # if current ele is smaller than stack top
            # find it's insert position
            while len(stack) != 0 and nums[idx] < stack[~0][0]:
                ele, ele_idx = stack.pop()
                # update subarray start
                sub_start = min(ele_idx, sub_start)
                sub_end   = max(idx, sub_end)
                
            # if subarray end is current idx
            # then, that means current element was smaller than stack top
            if sub_end == idx:
                # put stack top back
                stack.append([cur_top, cur_top_idx])
            else:
                # otherwise, simply push current element and it's index to stack
                stack.append([nums[idx], idx])
            
        # if subarray start was unchanged means array was sorted
        # and result is 0
        if sub_start == float('inf'): return 0
        return sub_end - sub_start + 1
'''

# Kunal Wadhwa

'''