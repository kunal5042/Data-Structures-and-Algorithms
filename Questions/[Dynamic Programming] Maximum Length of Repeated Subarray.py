# Question: https://leetcode.com/problems/maximum-length-of-repeated-subarray/
# Medium

from collections import defaultdict
from typing import List, Optional

class Solution:
    # brute-force O(max(n*n, m*m)) time and O(n*n + m*m) space
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        subarrays = defaultdict(int)
        
        def extract_subarrays(array):
            for idx in range(len(array)):
                subarray = ''
                for jdx in range(idx, len(array)):
                    subarray += str(array[jdx])
                    subarrays[subarray] += 1
                    
        extract_subarrays(nums1)
        extract_subarrays(nums2)
        
        longest_subarray = None
        for subarray, count in subarrays.items():
            if longest_subarray is None:
                longest_subarray = len(subarray)
                continue
                
            if count > 1:
                longest_subarray = max(longest_subarray, len(subarray))
                
        return longest_subarray
    
    # dynamic-programming: tabulation
    # O(n*m) time and O(n*m) space
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        memo = [[0 for _ in range(len(nums2))] for _ in range(len(nums1))]
        
        for row in range(len(nums1)):
            for col in range(len(nums2)):
                if nums1[row] == nums2[col]:
                    if row - 1 < 0 or col -1 < 0:
                        memo[row][col] = 1
                        continue
                        
                    memo[row][col] = 1 + memo[row-1][col-1]
                    
        return max(max(row) for row in memo)


# January 31, 2023

'''

# Kunal Wadhwa

'''