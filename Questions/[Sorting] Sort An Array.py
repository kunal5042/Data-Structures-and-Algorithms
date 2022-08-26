# Question: https://leetcode.com/problems/sort-an-array/
# Medium
from typing import Optional, List

from heapq import heapify, heappop, heappush
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # return self.heap_sort(nums)
        # self.quick_sort(0, len(nums)-1, nums)
        self.merge_sort(0, len(nums)-1, nums)
        return nums
        
    
    # Quick-Sort implementation
    # Theta(n * log(n)) Time
    # O(n ^ 2) Time 
    def quick_sort(self, start, end, arr):
        # base-case
        if start >= end: return
        
        pivot = arr[start]
        left  = start + 1
        right = end
        
        while right >= left:
            is_smaller, is_greater = arr[left], arr[right]
            
            if is_smaller > pivot and is_greater < pivot:
                self.swap(left, right, arr)
                left  += 1
                right -= 1
                continue
            
            if is_smaller <= pivot:
                left += 1
                
            if is_greater >= pivot:
                right -= 1
                
        self.swap(start, right, arr)
        self.quick_sort(right+1, end, arr)
        self.quick_sort(start, right-1, arr)
        
    # O(1) Time and O(1) Space
    def swap(self, x, y, arr):
        arr[x], arr[y] = arr[y], arr[x]
        
        
    # O(high - low + 1) Time and O(high - low + 1) Space
    def merge(self, low, middle, high, array):
        temp = []
        
        left, right = low, middle + 1
        
        while left <= middle and right <= high:
            if array[left] <= array[right]:
                temp.append(array[left])
                left += 1
                
            else:
                temp.append(array[right])
                right += 1
                
        # one array exhausted before the other
        while left <= middle:
            temp.append(array[left])
            left += 1
            
        while right <= high:
            temp.append(array[right])
            right += 1
            
        # copying back 
        for idx in reversed(range(low, high+1)):
            array[idx] = temp.pop()
            
    # O(n * log(n)) Time and O(n) Space
    def merge_sort(self, low, high, array):
        if low >= high: return
        middle = (low + high) // 2
        self.merge_sort(low, middle, array)
        self.merge_sort(middle+1, high, array)
        self.merge(low, middle, high, array)
        return
    
    # O(n * log(n)) Time and O(n) Space
    def heap_sort(self, array):
        heapify(array)
        sorted_array = []
        while len(array) != 0:
            sorted_array.append(heappop(array))
        return sorted_array
'''

# Kunal Wadhwa

'''