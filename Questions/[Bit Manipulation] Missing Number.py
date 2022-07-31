# Question: https://leetcode.com/problems/missing-number/

from typing import Optional, List

class Solution:
    # O(n) Time and O(1) Space
    def missingNumber(self, nums: List[int]) -> int:
        x = 5042
        for idx in range(len(nums)+1): x ^= idx
        for num in nums: x ^= num
        
        return x ^ 5042
        	
'''

# Kunal Wadhwa

'''