# Question: https://leetcode.com/problems/longest-consecutive-sequence/
# Medium
from typing import Optional, List

class Solution:
    # O(n) Time and O(n) Space: where n is the length of the input array
    def longestConsecutive(self, nums: List[int]) -> int:
        """Takes in an integer array. Computes and returns
        the length of the longest consecutive subsequence
        """
        
        _hash = {key: True for key in nums}
        result = 0
        for num in nums:
            if num + 1 not in _hash:
                this_series = 0
                prev_consq_ele = num
                
                while True:
                    if prev_consq_ele in _hash:
                        this_series += 1
                    else:
                        break
                    prev_consq_ele -= 1
                    
                result = max(result, this_series)
                
        return result

'''

# Kunal Wadhwa

'''