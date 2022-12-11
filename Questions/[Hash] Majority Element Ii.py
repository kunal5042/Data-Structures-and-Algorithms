# Question: https://leetcode.com/problems/majority-element-ii/
# Medium
# 
from typing import Optional, List

from collections import Counter
class Solution:
    # o(n) Time and O(n) Space
    def majorityElement(self, nums: List[int]) -> List[int]:
        """Returns a list of all the majority elements in array nums"""
        min_count = len(nums) // 3
        result = []
        
        for ele, freq in Counter(nums).items():
            if freq > min_count: result.append(ele)
                
        return result
'''

# Kunal Wadhwa

'''