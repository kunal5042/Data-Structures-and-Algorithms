# Question: https://leetcode.com/problems/count-good-triplets-in-an-array/
# Hard

import bisect
from sortedcontainers import SortedList
from typing import List

class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        pos = [0] * len(nums1)               
        for idx, b in enumerate(nums2):
            pos[b] = idx
        
        pos_in_nums2, pre_nums1 = SortedList([pos[nums1[0]]]), [0]      
        for a in nums1[1:]:       
            pos_in_nums2.add(pos[a])
            pre_nums1.append(pos_in_nums2.bisect_left(pos[a]))
    
        pos_in_nums2, suf_nums1 = SortedList([pos[nums1[-1]]]), [0]
        for a in reversed(nums1[:len(nums1)-1]):
            idx = pos_in_nums2.bisect(pos[a])
            suf_nums1.append(len(pos_in_nums2) - idx)
            pos_in_nums2.add(pos[a])
        suf_nums1.reverse()
        
        result = 0
        for x, y in zip(pre_nums1, suf_nums1):
            result += x * y
        return result


# January 31, 2023

'''

# Kunal Wadhwa

'''