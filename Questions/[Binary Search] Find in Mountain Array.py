# Question: https://leetcode.com/problems/find-in-mountain-array/
# Hard
from typing import Optional, List

# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    # O(log(n)) time and O(1) space
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        # find the peak
        peak = 0
        left, right = 0, mountain_arr.length()-1
        while left < right:
            middle = (left + right) // 2
            
            if mountain_arr.get(middle) < mountain_arr.get(middle+1):
                left = middle + 1
                peak = middle + 1
            else:
                right = middle
                
        print(peak)
        # search in left
        left, right = 0, peak
        while left <= right:
            middle = (left + right) // 2
            
            if mountain_arr.get(middle) == target:
                return middle 
            
            if mountain_arr.get(middle) > target:
                right = middle - 1
            else:
                left = middle + 1
                
        # search in right
        left, right = peak, mountain_arr.length()-1
        while left <= right:
            middle = (left + right) // 2
            
            if mountain_arr.get(middle) == target:
                return middle 
            
            if mountain_arr.get(middle) > target:
                left = middle + 1
            else:
                right = middle - 1
        return -1


# January 21, 2023

'''

# Kunal Wadhwa

'''