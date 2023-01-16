# Question: https://leetcode.com/problems/partition-to-k-equal-sum-subsets/
# Medium
from typing import Optional, List

class Solution:
    # O(n^k) time and O(n) space
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        array_sum = sum(nums)
        # quick-escape
        if array_sum % k != 0: return False
        
        target = array_sum // k
        subset = [0 for _ in range(k)]
        nums.sort(reverse=True)
        
        def valid_addition(idx):
            if idx == len(nums):
                for jdx in range(k):
                    if subset[jdx] != target:
                        return False
                return True
            
            for jdx in range(k):
                if subset[jdx] + nums[idx] <= target:
                    subset[jdx] += nums[idx]
                    if valid_addition(idx+1):
                        return True
                    subset[jdx] -= nums[idx]
                    
                    # bread and butter to get the solution accepted
                    if subset[jdx] == 0:
                        break
            
            return False
        return valid_addition(0)
                                


# January 16, 2023

'''

# Kunal Wadhwa

'''