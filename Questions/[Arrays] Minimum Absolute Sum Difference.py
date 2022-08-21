# Question: https://leetcode.com/problems/minimum-absolute-sum-difference/
# Medium
# Took some time!
from typing import Optional, List

from bisect import bisect_left as closest_number_idx
class Solution:
    # O(n log(n)) Time and O(n) Space
    def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:
        LENGTH = len(nums1)
        sorted_nums1 = sorted(nums1)
        largest_reduced_difference = float('-inf')
        largest_reduced_difference_idx = None
        reduced_difference = None
        
        for idx in range(LENGTH):
            original = abs(nums1[idx] - nums2[idx])
            if original == 0: continue
            
            jdx = closest_number_idx(sorted_nums1, nums2[idx])
            if jdx != 0 and jdx != LENGTH:
                optimized = abs(sorted_nums1[jdx] - nums2[idx])
                optimized = min(optimized, abs(sorted_nums1[jdx-1] - nums2[idx]))
            if jdx == 0:
                optimized = abs(sorted_nums1[jdx] - nums2[idx])
            if jdx == LENGTH:
                optimized = abs(sorted_nums1[jdx-1] - nums2[idx])
                
            if original == optimized: continue
            
            this = abs(original - optimized)
            
            if this > largest_reduced_difference:
                largest_reduced_difference = this
                largest_reduced_difference_idx = idx
                reduced_difference = optimized
    
        if largest_reduced_difference == float('-inf'): return 0        
        
        total = 0
        for idx in range(LENGTH):
            if idx == largest_reduced_difference_idx:
                total += reduced_difference
            else:
                total += abs(nums1[idx] - nums2[idx])
        return total % (10**9 + 7)
    
    # Greedy Approach: Earlier it got accepted at LC but it doesn't work
    #
    # Sample Input:
    # nums1: [10, 13, 9]
    # nums2: [2,   7, 9]
    # Expected => 10
    # Output   => 13
    #
    # O(n) Time and O(1) Space
    def minAbsoluteSumDiff_Greedy(self, nums1: List[int], nums2: List[int]) -> int:
        LENGTH = len(nums1)
        
        # [maximum difference, idx it comes from]
        max_diff = [0, None]
        total    = 0
        
        for idx in range(LENGTH):
            cur_diff = abs(nums1[idx]-nums2[idx])
            total    += cur_diff
            if cur_diff > max_diff[0]:
                max_diff[0] = cur_diff
                max_diff[1] = idx
            
        # early return
        if max_diff[0] == 0: return 0
        
        # print(total, max_diff[0])
        # we'll try to minimize
        total -= max_diff[0]
        
        # 
        target  = nums2[max_diff[1]]
        closest = None
        for idx in range(LENGTH):
            if closest is None: closest = nums1[idx]
            if abs(nums1[idx] - target) < abs(closest - target):
                closest = nums1[idx]
                
        total += abs(target - closest)
        return total % (10**9 + 7)
    
    
'''

# Kunal Wadhwa

'''