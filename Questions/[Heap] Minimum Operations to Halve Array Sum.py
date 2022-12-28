# Question: https://leetcode.com/problems/minimum-operations-to-halve-array-sum/
# Medium
from typing import Optional, List
from heapq import heapify, heappop, heappush

class Solution:
    # O(n * log(n)) time and O(n) space
    def halveArray(self, nums: List[int]) -> int:
        (total, target) = (0, 0)
        heap  = []
        
        for idx in range(len(nums)):
            total += nums[idx]
            heap.append(-nums[idx])
            
        target = total / 2
        
        heapify(heap)
        operations = 0
        while total > target and len(heap) > 0:
            reduced = abs(heappop(heap)) / 2
            total -= reduced
            heappush(heap, -reduced)
            operations += 1

        return operations


# December 28, 2022

'''

# Kunal Wadhwa

'''