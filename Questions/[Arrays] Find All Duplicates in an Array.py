# Question: https://leetcode.com/problems/find-all-duplicates-in-an-array/
# Medium
# Map indices to numbers 
from typing import List, Optional

class Solution:
    # O(n) Time and O(1) Space
    def findDuplicates(self, nums: List[int]) -> List[int]:
        result = list()
        
        for number in nums:
            
            idx = abs(number) - 1
            
            if nums[idx] < 0:
                result.append(abs(number))
                
            else:
                nums[idx] = -1 * nums[idx]
                
                
        return result
    
# Kunal Wadhwa