# Question: https://leetcode.com/problems/peak-index-in-a-mountain-array/
# Medium
# Direction is the key
from typing import Optional, List

class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        """Takes a mountain array as input
        Finds and returns the index of the peak element in this array
        """
        start, end = 0, len(arr)-1
        
        # mountain condition
        while end - start + 1 >= 3:
            middle = (start+end)//2
            
            if arr[middle] > arr[middle-1] and arr[middle] > arr[middle+1]:
                return middle
            
            if arr[middle] > arr[middle-1]:
                start = middle
            else:
                end   = middle
                
        return "We'll never reach here"
    
'''

# Kunal Wadhwa

'''