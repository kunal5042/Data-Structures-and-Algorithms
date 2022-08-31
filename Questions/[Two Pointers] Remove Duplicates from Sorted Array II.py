# Question: https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/
# Medium
from typing import Optional, List

class Solution:
    # O(n) Time and O(1) Space
    def removeDuplicates(self, nums: List[int]) -> int:
        buffer  = nums[0]
        unique  = 1
        pointer = 1
        
        for idx in range(1, len(nums)):
            if nums[idx] == buffer:
                unique += 1
            else:
                buffer = nums[idx]
                unique = 1
                
            if unique > 2: continue
            
            nums[pointer] = buffer
            pointer += 1
            
        return pointer
'''

# Kunal Wadhwa

'''