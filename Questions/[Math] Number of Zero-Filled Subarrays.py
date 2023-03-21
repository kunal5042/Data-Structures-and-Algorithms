# Question: https://leetcode.com/problems/number-of-zero-filled-subarrays/
# Medium

from typing import List

class Solution:
    # O(n) time and O(1) space
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        sub_len = 0
        result = 0
        
        for ele in nums:
            if ele == 0:
                sub_len += 1
            else:
                result += sub_len*((sub_len+1)/2)
                sub_len = 0
                
        result += sub_len*((sub_len+1)/2)
        return int(result)


# March 21, 2023

'''

# Kunal Wadhwa

'''