# Question: https://leetcode.com/problems/sliding-window-maximum/
# Hard

from heapq import heappush, heapify, heappop
from typing import List

class Solution:
    # O(n*log(n)) time and O(n) space
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = [(-nums[idx], idx) for idx in range(k)]
        heapify(heap)
        
        result = [0 for _ in range(len(nums)-k+1)]
        result[0] = -1*(heap[0][0])
        
        for idx in range(k, len(nums)):
            heappush(heap, (-nums[idx], idx))
            
            while heap[0][1] < idx - k + 1:
                heappop(heap)
                
            result[idx-k+1] = -1*(heap[0][0])
            
        return result


# February 04, 2023

'''

# Kunal Wadhwa

'''