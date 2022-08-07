# Question: https://leetcode.com/problems/target-sum/

from typing import Optional, List

class Solution:
    # brute-force approach
    # O(2^n) Time and O(n) Space
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        can_build = [0]
        
        def helper(run_sum, next_idx):
            if run_sum == target and next_idx == len(nums): can_build[0] += 1
            if next_idx >= len(nums): return
            
            helper(run_sum + nums[next_idx], next_idx + 1)
            helper(run_sum - nums[next_idx], next_idx + 1)
            
            
        helper(0, 0)
        return can_build[0]
    
    # dynamic-programming with memoization
    # O(n) Time and O(n) Space
    def findTargetSumWays(self, nums, target) -> int:
        # store solutions to the sub-problems
        memo = {}
        
        def helper(run_sum, next_idx):
            path = (run_sum, next_idx)
            
            # if we have seen this path before
            if path in memo: return memo[path]
                
            # return True to the parent path
            if run_sum == target and next_idx == len(nums):
                return 1
            
            # return False to the parent path
            if next_idx >= len(nums):
                return 0
            
            # child call will return the count of paths that returned True
            addition_path = helper(run_sum + nums[next_idx], next_idx + 1)
            subtract_path = helper(run_sum - nums[next_idx], next_idx + 1)
            
            # store the result of this path/sub-problem
            memo[(run_sum, next_idx)] = addition_path + subtract_path
            
            # return solution to this sub-problem
            return memo[(run_sum, next_idx)]
        
        return helper(0, 0)	
'''

# Kunal Wadhwa

'''