# Question: https://leetcode.com/problems/find-the-k-sum-of-an-array/
# Hard

from heapq import heappush, heappop
from typing import List

class Solution:
    # brute-force
    def kSum(self, nums: List[int], k: int) -> int:
        heap = []
        
        def subseq_sums(idx, csum):
            if idx == len(nums):
                heap.append(csum)
                return
            
            subseq_sums(idx+1, csum+nums[idx])
            subseq_sums(idx+1, csum)
            
        subseq_sums(0, 0)
        heap.sort()
        return heap[~(k-1)]

    # O(n*log(n) + k*log(k)) time and O(n + k) space
    def kSum(self, nums: List[int], k: int) -> int:
        max_sum = sum([max(ele, 0) for ele in nums])
        values = sorted([abs(ele) for ele in nums])
        
        min_remove = 0
        heap = [(values[0], 0)]
        
        # at every step, we generate the next smallest sum
        # that we can take away from the maxsum
        for _ in range(k-1):
            min_remove, idx = heappop(heap)
            
            if idx + 1 < len(values):
                heappush(heap, (min_remove + values[idx+1], idx+1))
                heappush(heap, (min_remove + values[idx+1] - values[idx], idx+1))
                
        return max_sum - min_remove


# February 05, 2023

'''

# Kunal Wadhwa

'''