# Question: https://leetcode.com/problems/rotate-array/
# Medium
# Reverse(Reverse[0:k], Reverse[k+1:])
from typing import Optional, List

class Solution:
    # O(n) Time and O(k) Space
    def rotate(self, nums: List[int], k: int) -> None:
        """Given an integer array nums, and an integer k
        Rotates the given array k times in place
        """
        if k == 0 or k % len(nums) == 0: return
        k = k % len(nums) if k >= len(nums) else k
        
        cache = nums[-k:]
        
        _from = len(nums) - k - 1
        _to   = len(nums) - 1
        
        while _from > -1:
            nums[_to] = nums[_from]
            _to   -= 1
            _from -= 1
            
        for idx in range(len(cache)):
            nums[idx] = cache[idx]
            
        return
    
    # O(n) Time and O(1) Space
    def rotate(self, nums: List[int], k: int) -> None:
        """Given an integer array nums, and an integer k
        Rotates the given array k times in place
        """
        if k == 0 or k % len(nums) == 0: return
        k = k % len(nums) if k >= len(nums) else k
        
        def reverse(start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end   -= 1
            return
        
        reverse(0, len(nums) -k - 1)
        reverse(len(nums) - k, len(nums) - 1)
        reverse(0, len(nums)-1)
        return
'''

# Kunal Wadhwa

'''