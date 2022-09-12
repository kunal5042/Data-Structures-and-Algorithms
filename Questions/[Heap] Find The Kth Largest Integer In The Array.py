# Question: https://leetcode.com/problems/find-the-kth-largest-integer-in-the-array/
# Medium
# To Do: Implement linear time
from typing import Optional, List

from heapq import heapify, heappop, heappush

class Solution:
    # O(n * log(n)) Time and O(n) Space
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        heap = []
        heapify(heap)
        
        for idx in range(len(nums)):
            heappush(heap, -1 * int(nums[idx]))

        for _ in range(k-1): heappop(heap)
            
        return str(-1 * heappop(heap))
'''

# Kunal Wadhwa

'''