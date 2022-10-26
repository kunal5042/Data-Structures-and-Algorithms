# Question: https://leetcode.com/problems/find-k-pairs-with-smallest-sums/
# Medium
from typing import Optional, List
from heapq import heappop, heappush
class Solution:
    # O(k * log(k)) Time
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        # smallest-sum-pair
        heap = [(nums1[0] + nums2[0], 0, 0)]
        visited = set([(0, 0)])
        output = []
        
        # extract k pairs as long as pairs are available
        while len(output) != k and len(heap) != 0:
            _sum, x, y = heappop(heap)
            output.append((nums1[x], nums2[y]))
            
            # potential next smallest-sum-pair as both arrays are sorted
            if x + 1 < len(nums1) and (x+1, y) not in visited:
                heappush(heap, (nums1[x+1] + nums2[y], x+1, y))
                
                # avoid duplications
                # like (0,1) -> (1,1) and (0,2) 
                # and  (1,0) -> (1,1) and (2,0)
                # (1,1) is overlapping
                visited.add((x+1, y))

            # same as above, add potential next smallest-sum-pair to the pq
            if y + 1 < len(nums2) and (x, y+1) not in visited:
                heappush(heap, (nums1[x] + nums2[y+1], x, y+1))
                visited.add((x, y+1))
            
        return output
'''

# Kunal Wadhwa

'''