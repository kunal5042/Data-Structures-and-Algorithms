# Question: https://leetcode.com/problems/longest-increasing-subsequence/
# Medium

from typing import Optional, List

class Solution:
    # O(n^2) Time and O(n) Space
    def lengthOfLIS(self, nums: List[int]) -> int:
        len_lis = [1 for _ in range(len(nums))]
        result  = 1
        
        for idx in range(1, len(nums)):
            for jdx in reversed(range(0, idx)):
                
                # extend current lis
                if nums[jdx] < nums[idx]:
                    len_lis[idx] = max(len_lis[idx], 1 + len_lis[jdx])
                    result = max(len_lis[idx], result)
            
        return result
'''

# Kunal Wadhwa

'''