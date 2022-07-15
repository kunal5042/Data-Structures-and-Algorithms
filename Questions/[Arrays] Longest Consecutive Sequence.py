# Question: https://leetcode.com/problems/longest-consecutive-sequence/

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
# Question: https://leetcode.com/problems/longest-consecutive-sequence/

class Solution:
    def longestConsecutive(self, nums):
        if len(nums) == 0:
            return 0
        
        hash   = set(nums)
        result = 0

        for num in nums:
            
            if (num-1) not in hash:
                target, current = num, 0

                while True:
                    if target in hash:
                        target  += 1
                        current += 1
                    else:
                        break

                result = max(result, current)
            
            
        return result
                
# Kunal Wadhwa'''

# Kunal Wadhwa

'''