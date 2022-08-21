# Question: https://leetcode.com/problems/intersection-of-two-arrays/
# Easy
#
from typing import Optional, List

class Solution:
    # O(max(n, m)) Time and O(min(n, m)) Space
    # where n is the length of the nums1
    # and m is the length of the nums2
    
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        smaller, larger = nums1, nums2
        if len(nums1) > len(nums2):
            smaller, larger = nums2, nums1
            
        set_smaller = set(smaller)
        visited = set()
        result  = []
        
        for ele in larger:
            if ele in set_smaller and ele not in visited:
                visited.add(ele)
                result.append(ele)
                
        return result
    
    
'''

# Kunal Wadhwa

'''