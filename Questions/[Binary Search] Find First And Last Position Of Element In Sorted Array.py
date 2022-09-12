# Question: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
# Medium

from typing import Optional, List

class Solution:
    # O(log(n)) Time and O(1) Space
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        """Takes a sorted list of integers and an integer target.
        Finds out the range in which the target integer is present in the sorted list.
        Returns the start and end index of this range
        """
        result = [float('inf'), float('-inf')]
        found  = False
        
        def binary_search(start, end):
            nonlocal found
            
            while start <= end:
                middle = (start + end) // 2
                
                if nums[middle] == target:
                    found = True
                    result[0] = min(result[0], middle)
                    result[1] = max(result[1], middle)
                    
                    binary_search(start   , middle-1)
                    binary_search(middle+1, end)
                    
                    return
                
                if nums[middle] > target:
                    end = middle - 1
                else:
                    start = middle + 1
                    
        binary_search(0, len(nums)-1)
        if not found: return [-1, -1]
        return result
'''

# Kunal Wadhwa

'''