# Question: https://leetcode.com/problems/sum-of-subarray-ranges**/

from typing import Optional, List

class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, val):
        self.stack.append(val)
        
    def empty(self):
        return len(self.stack) == 0
    
    def pop(self):
        if not self.empty():
            return self.stack.pop()
    
    def top(self):
        if not self.empty():
            return self.stack[~0]
        
    def pop_all(self):
        self.stack.clear()
        
class Solution:
    # O(n) Time and O(n) Space
    def subArrayRanges(self, nums: List[int]) -> int:
        
        next_greater = [None] * len(nums)
        prev_greater = [None] * len(nums)
        
        next_smaller = [None] * len(nums)
        prev_smaller = [None] * len(nums)
        
        # next greater element's index for each element
        stack  = Stack()
        for idx in reversed(range(len(nums))):
            while not stack.empty():
                if nums[stack.top()] > nums[idx]:
                    break
                stack.pop()
                
            next_greater[idx] = len(nums) if stack.empty() else stack.top()
            stack.push(idx)
            
        # previous greater element's index for each element
        stack.pop_all()
        for idx in range(len(nums)):
            while not stack.empty():
                if nums[stack.top()] >= nums[idx]:
                    break
                stack.pop()
                
            prev_greater[idx] = -1 if stack.empty() else stack.top()
            stack.push(idx)
            
        
        # next smaller element's index for each element
        stack.pop_all()
        for idx in reversed(range(len(nums))):
            while not stack.empty():
                if nums[stack.top()] < nums[idx]:
                    break
                stack.pop()
            
            next_smaller[idx] = len(nums) if stack.empty() else stack.top()
            stack.push(idx)
            
        # previous smaller element's index for each element
        stack.pop_all()
        for idx in range(len(nums)):
            while not stack.empty():
                if nums[stack.top()] <= nums[idx]:
                    break
                stack.pop()
                
            prev_smaller[idx] = -1 if stack.empty() else stack.top()
            stack.push(idx)
            
        _range = 0
        for idx in range(len(nums)):
            # number of sub-arrays in which current element is smallest
            smallest_count = (((next_smaller[idx] - 1) - idx) + 1) * ((idx - (prev_smaller[idx] + 1)) + 1)
            negative_contribution = smallest_count * nums[idx]
            
            # number of sub-arrays in which current element is largest
            largest_count = (((next_greater[idx] - 1) - idx) + 1) * ((idx - (prev_greater[idx] + 1)) + 1)
            positive_contribution = largest_count * nums[idx]
            
            _range += (positive_contribution - negative_contribution)

        return _range
'''

# Kunal Wadhwa

'''