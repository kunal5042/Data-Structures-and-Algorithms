# Question: https://leetcode.com/problems/count-nice-pairs-in-an-array/
# Medium
from typing import Optional, List

class Solution:
    # O(n*n) time and O(n) space
    def countNicePairs(self, nums: List[int]) -> int:
        def reverse(num):
            result = 0
            while num != 0:
                result *= 10
                result += num % 10
                num  = num // 10
            return result
        
        for idx in range(len(nums)):
            nums[idx] = nums[idx] - reverse(nums[idx])
            
        pairs = 0
        for idx in range(len(nums)):
            for jdx in range(idx+1, len(nums)):
                if nums[idx] == nums[jdx]:
                    pairs += 1
                    
        return pairs % (10**9 + 7)
    
    # optimizing the calculation of number of pairs using hashmap
    # O(n) time and O(n) space
    def countNicePairs(self, nums: List[int]) -> int:
        def reverse(num):
            result = 0
            while num != 0:
                result *= 10
                result += num % 10
                num  = num // 10
            return result
        
        for idx in range(len(nums)):
            nums[idx] = nums[idx] - reverse(nums[idx])
            
        hash_ = {}
        pairs = 0
        for value in nums:
            if value in hash_:
                pairs += hash_[value]
                hash_[value] += 1
            else:
                hash_[value] = 1
        
        return pairs % (10**9 + 7)
            	


# January 10, 2023

'''

# Kunal Wadhwa

'''