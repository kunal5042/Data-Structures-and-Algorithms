# Question: https://leetcode.com/problems/intersection-of-two-arrays-ii/
# Easy
# 
from typing import Optional, List

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        _hash1, _hash2 = {}, {}
        
        for ele in nums1: _hash1[ele] = _hash1.get(ele, 0) + 1
        for ele in nums2: _hash2[ele] = _hash2.get(ele, 0) + 1
            
        result = []
        
        for key, freq in _hash1.items():
            if key in _hash2:
                for _ in range(min(_hash2[key], freq)):
                    result.append(key)
                    
        return result
'''

# Kunal Wadhwa

'''