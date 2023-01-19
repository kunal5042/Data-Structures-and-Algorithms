# Question: https://leetcode.com/problems/subarray-sums-divisible-by-k/
# Medium
from typing import Optional, List

class Solution:
    # O(n) time and O(n) space
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        # the idea is that 
        # x = k*d1 + r1
        # y = k*d2 + r2
        # (x + y) % k == r1 + r2
        
        prefix = 0
        subarrays = 0
        seen = defaultdict(int)
        seen[0] = 1
        
        for num in nums:
            # to handle negative numbers as well
            prefix = (prefix + num%k + k) % k
            subarrays += seen[prefix]
            seen[prefix] += 1
            
        return subarrays
            
        


# January 19, 2023

'''

# Kunal Wadhwa

'''