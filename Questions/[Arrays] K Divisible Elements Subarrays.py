# Question: https://leetcode.com/problems/k-divisible-elements-subarrays/
# Medium
from typing import Optional, List

class Solution:
    # O(n*n) time and O(n*n) space: brute-force is accpeted 🙂
    def countDistinct(self, nums: List[int], k: int, p: int) -> int:
        subarrays = set()
        
        for idx in range(len(nums)):
            div_count = 0
            if nums[idx] % p == 0: div_count += 1
            subarray = [nums[idx]]
            subarrays.add(tuple(subarray))
            
            for jdx in range(idx+1, len(nums)):
                if nums[jdx] % p == 0: div_count += 1
                if div_count > k: break
                subarray.append(nums[jdx])
                subarrays.add(tuple(subarray))
                            
        return len(subarrays)


# January 26, 2023

'''

# Kunal Wadhwa

'''