# Question: https://leetcode.com/problems/last-stone-weight/
# Easy

from heapq import heapify, heappush, heappop
from typing import List

class Solution:
    # O(n*log(n)) time and O(n) space
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Create a max-heap of negative weights
        heap = [-weight for weight in stones] 
        heapify(heap) 
        
        # Keep removing the two largest elements from the heap
        # and inserting the difference back into the heap until
        # there is only one element left
        while len(heap) > 1: 
            largest = -heappop(heap) 
            second_largest = -heappop(heap) 
            
            result = largest - second_largest
            if result != 0:
                heappush(heap, -result) # O(logn)
                
        # If there is one element left in the heap, return it
        # (this will be the last stone's weight)
        # Otherwise, there are no stones left, so return 0
        return -heap[0] if len(heap) != 0 else 0


# April 24, 2023

'''

# Kunal Wadhwa

'''