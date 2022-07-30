# Question: https://leetcode.com/problems/combination-sum/

from typing import Optional, List

class Solution:
    # O(len(nums)^target) Time complexity
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """Returns all possible combinations of candidates that sum up to target"""
        result = []
        
        def helper(comb, _sum, start):
            if _sum == target:
                result.append(comb.copy())
                return
            
            for idx in range(start, len(candidates)):
                if candidates[idx] + _sum <= target:
                    comb.append(candidates[idx])
                    helper(comb, _sum + candidates[idx], idx)
                    comb.pop()
                    
            return
        
        
        helper([], 0, 0)
        return result
'''

# Kunal Wadhwa

'''