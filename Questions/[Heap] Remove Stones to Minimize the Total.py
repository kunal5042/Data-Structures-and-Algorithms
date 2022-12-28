# Question: https://leetcode.com/problems/remove-stones-to-minimize-the-total/
# Medium
from typing import Optional, List

from heapq import heapify, heappop, heappush
class Solution:
    # O(n * log(n)) time and O(n) space
    def minStoneSum(self, piles: List[int], k: int) -> int:
        heap = []
        
        for idx in range(len(piles)):
            heap.append(-piles[idx])
            
        heapify(heap)
        while k > 0 and len(heap) > 0:
            heappush(heap, -abs(heappop(heap)) // 2)
            k -= 1
            
        return -sum(heap)


# December 28, 2022

'''

# Kunal Wadhwa

'''