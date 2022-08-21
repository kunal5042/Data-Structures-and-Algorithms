# Question: https://leetcode.com/problems/combinations/
# Medium
# 
from typing import Optional, List

class Solution:
    # O(k (n choose k)) Time
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums   = list(range(1, n+1))
        result = []
        
        def combinations(choose, this_combination):
            if len(this_combination) == k:
                result.append(this_combination.copy())
                return
            
            # we'll not proceed further
            if choose >= len(nums):
                return
            
            for idx in range(choose, len(nums)):
                this_combination.append(nums[idx])
                combinations(idx+1, this_combination)
                this_combination.pop()
                
            return result
        
        return combinations(0, [])
'''

# Kunal Wadhwa

'''