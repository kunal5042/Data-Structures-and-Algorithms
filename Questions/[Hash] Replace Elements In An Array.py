# Question: https://leetcode.com/problems/replace-elements-in-an-array/

from typing import Optional, List

class Solution:
    # O(n) Time and O(n) Space
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        _hash = {}
        for idx, ele in enumerate(nums):
            _hash[ele] = idx
            
        for target, replace in operations:
            # replace the element
            replace_idx = _hash[target]
            nums[replace_idx] = replace

            # update the map
            _hash[replace] = replace_idx
            del _hash[target]
            
        return nums
'''

# Kunal Wadhwa

'''