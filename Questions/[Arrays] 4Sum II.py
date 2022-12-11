# Question: https://leetcode.com/problems/4sum-ii/
# Medium
from typing import Optional, List

class Solution:
    # bruteforce
    # O(n*n*n*n) Time and O(1) Space
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        LENGTH = len(nums1)
        output = 0
        for i in range(LENGTH):
            for j in range(LENGTH):
                for k in range(LENGTH):
                    for l in range(LENGTH):
                        if nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0:
                            output += 1
        return output
    
    # O(n*n) Time and O(n*n) Space
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
            output = 0
            LENGTH = len(nums1)
            pairs = defaultdict(int)
            for i in range(LENGTH):
                for j in range(LENGTH):
                    pairs[nums1[i] + nums2[j]] += 1
                    
            for k in range(LENGTH):
                for l in range(LENGTH):
                    output += pairs[-(nums3[k] + nums4[l])]
            
            return output
    
    	
'''

# Kunal Wadhwa

'''