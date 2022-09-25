# Question: https://leetcode.com/problems/divide-intervals-into-minimum-number-of-groups/
# Medium
from typing import Optional, List

class Solution:
    # Brute Force
    # O(n^2) Time and O(n) Space
    def minGroups(self, intervals: List[List[int]]) -> int:
        groups = []
        heapify(intervals)
        
        while len(intervals) != 0:
            start, end = heappop(intervals)
            
            if len(groups) == 0:
                groups.append([start, end])
                continue
                
            new_group = True
            for idx in range(len(groups)):
                gstart, gend = groups[idx]
                
                if start > gend:
                    groups[idx][0] = min(start, gstart)
                    groups[idx][1] = max(end, gend)
                    new_group = False
                    break
                    
            if new_group is True:
                groups.append([start, end])
                
        return len(groups)
    
    # O(n) Time and O(n) Space - where is the length of the intervals array
    def minGroups(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        heap = []
        
        for start, end in intervals:
            if len(heap) != 0 and heap[0] < start:
                heappop(heap)
                
            heappush(heap, end)
            
        return len(heap)
'''

# Kunal Wadhwa

'''