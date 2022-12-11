# Question: https://leetcode.com/problems/continuous-subarray-sum/
# Medium
from typing import Optional, List

class Solution:
    # brute-force approach
    # O(n*n) Time and O(1) Space
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        for idx in range(len(nums)):
            _sum = nums[idx]
            for jdx in range(idx+1, len(nums)):
                _sum += nums[jdx]
                if _sum % k == 0:
                    return True
                
        return False
    
    # using prefix sum
    # intuition
    # As we traverse the array, we compute the prefix sums
    # At every step, we compute prefix_sum % k and check if the remainder
    # has been seen before
    # Because, if it has been seen before, there must be a multiple of k 
    # added to it from the last seen position, as the remainders are same
    
    # O(n) Time and O(1) Space
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        seen = {0:0}
        prefix = 0
        for idx in range(len(nums)):
            prefix += nums[idx]
            remainder = prefix % k
            
            if remainder not in seen:
            # idx + 1, because the multiple elements will/might be added after this remainder
                seen[remainder] = idx + 1
                continue
            
            if seen[remainder] < idx:
                return True
            
        return False
'''

# Kunal Wadhwa

'''