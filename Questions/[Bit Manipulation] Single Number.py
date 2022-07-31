# Question: https://leetcode.com/problems/single-number/

from typing import Optional, List

class Solution:
    # O(n) Time and O(1) Space
    def singleNumber(self, nums: List[int]) -> int:
        result = nums[0]
        
        # Logic: Duplicate numbers will XOR with self and turn into 0
        
        for idx in range(1, len(nums)):
            result ^= nums[idx]
            
        
        return result	
'''

# Kunal Wadhwa

'''