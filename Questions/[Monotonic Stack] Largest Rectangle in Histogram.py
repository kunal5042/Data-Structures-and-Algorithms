# Question: https://leetcode.com/problems/largest-rectangle-in-histogram/
# Hard
from typing import Optional, List

class Solution:
    # Solution - 1
    # for every bar we calculate the index of the next bar which is smaller than the current bar
    # and the previous bar which is smaller than the current
    # we assume the current bar as the limiting bar
    # using the indices of next and previous smaller bars we calculate the width
    # using this width and the height of the current bar we calculate the area
    # we keep track of the maximum area
    
    # O(3*n) time and O(2*n) space
    def largestRectangleArea(self, heights: List[int]) -> int:
        next_smaller = [len(heights) for _ in range(len(heights))]
        stack = []
        
        for idx in reversed(range(len(heights))):
            while len(stack) != 0 and heights[stack[~0]] >= heights[idx]:
                stack.pop()
                
            if len(stack) != 0:
                next_smaller[idx] = stack[~0]
                
            stack.append(idx)
            
        prev_smaller = [-1 for _ in range(len(heights))]
        stack = []
        
        for idx in range(len(heights)):
            while len(stack) != 0 and heights[stack[~0]] >= heights[idx]:
                stack.pop()
                
            if len(stack) != 0:
                prev_smaller[idx] = stack[~0]
                
            stack.append(idx)
            
        largest_rectangle = float('-inf')

        for idx in range(len(heights)):
            this_rectangle = (next_smaller[idx] - prev_smaller[idx] - 1) * heights[idx]
            largest_rectangle = max(largest_rectangle, this_rectangle)
            
        return largest_rectangle
    
    # Solution - 2
    # we maintain a monotonic increasing stack
    # when we find an element which is smaller than stack top
    # we do this
        # we pop the top and assume it as the limiting bar in the rectangle
        # the current element is smaller than stack top, hence we can form the rectangle 
        # to a position of one minus the current position 
        # we use this to calculate width
        # we use height and width to calculate the area and keep track of the maximum
        # we do these steps as long as stack top is greater than current element
    # why this work?
    # because the stack is monotonic in nature
    # every time we pop the top and use it as the limiting bar
    # we are calculating every rectangle area that we can form if the rectangle ended one position before
    # the current bar
    # that's why we add a zero to the end, so that rectangles can end on the last bar too
    # otherwise that case would have been missed
    
    # O(n) time and O(n) space
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        largest_rectangle = 0
        heights.append(0)
        
        for idx in range(len(heights)):
            while len(stack) != 0 and heights[stack[~0]] >= heights[idx]:
                smallest_bar = heights[stack.pop()]
                width = idx if len(stack) == 0 else idx - stack[~0] - 1
                largest_rectangle = max(largest_rectangle, smallest_bar * width)
                
            stack.append(idx)
            
        return largest_rectangle


# December 20, 2022

'''

# Kunal Wadhwa

'''