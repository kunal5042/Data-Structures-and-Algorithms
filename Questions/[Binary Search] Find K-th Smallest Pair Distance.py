# Question: https://leetcode.com/problems/find-k-th-smallest-pair-distance/
# Hard

from typing import List

class Solution:
    #
    # O(N * log(W) + N * log(N)) time and O(1) space
    # where 
    # n = length of the nums
    # w = number of iterations in binary search
    #
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        def is_pairs_greater_than_k(guess):
            start = 0
            pairs = 0
            for end in range(1, len(nums)):
                while nums[end] - nums[start] > guess:
                    start += 1
                pairs += end - start
            return pairs >= k
        
        nums.sort()
        low = 0
        high = abs(nums[~0] - nums[0])
        
        while low < high:
            middle = (low + high) // 2
            if is_pairs_greater_than_k(middle):
                high = middle
            else:
                low = middle + 1
        
        return low


# May 05, 2023

'''

# Kunal Wadhwa

'''