# Question: https://leetcode.com/problems/max-consecutive-ones-iii/
# Medium
# To Do: Optimize Space

from typing import Optional, List
from collections import deque

class Solution:
    # O(n) Time and O(n) Space
    def longestOnes(self, nums: List[int], k: int) -> int:
        result = 0
        
        zeroes = deque()
        start = end = flips = 0
        
        while end < len(nums):
            if nums[end] == 0:
                zeroes.append(end)

                if flips < k:
                    flips += 1
                else:
                    start = zeroes.popleft() + 1
                    
            result = max(result, end - start + 1)
            end += 1
            
        return result
'''

# Kunal Wadhwa

'''