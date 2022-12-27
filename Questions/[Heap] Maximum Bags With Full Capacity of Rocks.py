# Question: https://leetcode.com/problems/maximum-bags-with-full-capacity-of-rocks/
# Medium
from typing import Optional, List

from heapq import heapify, heappop, heappush
class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additional_rocks: int) -> int:
        heap = []
        for max_cap, cap_used in zip(capacity, rocks):
            heap.append(max_cap-cap_used)
            
        heapify(heap)
        full_bags = 0
        while len(heap) != 0 and additional_rocks != 0:
            space = heappop(heap)
            if space == 0:
                full_bags += 1
                continue
            
            if space <= additional_rocks:
                additional_rocks -= space
                full_bags += 1 
        
        return full_bags


# December 27, 2022

'''

# Kunal Wadhwa

'''