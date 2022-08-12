# Question: https://leetcode.com/problems/kth-largest-element-in-an-array/

from typing import Optional, List

# Quick Select Implementation
class QuickSelect:
    def __init__(self, array, position):
        self.smallest_idx   = position - 1
        self.largest_idx    = len(array) - position
        self.correct_idx    = None
        self.selected       = None
        self.select(0, len(array)-1, array, False)
        
        
    # Takes in 4 variables
    # start and end specify the window size of the quick select algorithm
    # array is the list on which quick select will be performed
    # if smallest is True the smallest element for the given position will be selected
    # otherwise the largest element for the given position will be selected
    def select(self, start, end, array, smallest=True):
        if smallest:
            self.correct_idx = self.smallest_idx
        else:
            self.correct_idx = self.largest_idx
        
        while True:
            left, right = start+1, end
            pivot       = array[start]

            while left <= right:
                if array[left] > pivot and array[right] < pivot:
                    self.swap(left, right, array)
                    left  += 1
                    right -= 1

                elif array[right] >= pivot:
                    right -= 1

                else:
                    left  += 1

            # put pivot in it's correct position
            self.swap(start, right, array)

            
            # if pivot was put in desired position
            # we selected the element we wanted
            # break
            if array[self.correct_idx] == pivot:
                self.selected = pivot
                break

            # pivot was put towards the right of the desired index
            # which implies that all the elements towards the right-side of the pivot index i.e right, will be greater than the pivot
            # our desired element must be smaller than pivot as pivot is in it's correct position and is towards right of the desired index
            # we can eliminate the right part, as it cannot contain our desired element
            if right > self.correct_idx:
                start, end = 0, right -1
            else:
                # similarly we can eliminate the left part
                start, end = right + 1, len(array)-1
                
                    
    def swap(self, x, y, array):
        array[x], array[y] = array[y], array[x]

        

class Solution:
    # Using Quick Select Algorithm
    # O(n) Time (Average) and O(1) Space
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if k == len(nums): return min(nums)
        if k == 1        : return max(nums)
        
        return QuickSelect(nums, k).selected
        
# Kunal Wadhwa
