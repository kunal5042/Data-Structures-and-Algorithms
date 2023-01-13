# Question: https://leetcode.com/problems/query-kth-smallest-trimmed-number/
# Medium
from typing import Optional, List

class Solution:
    # O(n * m) time and O(n) space
    def smallestTrimmedNumbers(self, nums: List[str], queries: List[List[int]]) -> List[int]:
        result = [None for _ in range(len(queries))]
        
        for idx, (kth, trim) in enumerate(queries):
            array = []
            for jdx, num_string in enumerate(nums):
                array.append((num_string[-trim:], jdx))
                
            array.sort()
            result[idx] = array[kth-1][1]
        
        return result


# January 13, 2023

'''

# Kunal Wadhwa

'''