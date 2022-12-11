# Question: https://leetcode.com/problems/non-overlapping-intervals/
# Medium

from typing import Optional, List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals) <= 1: return 0
        intervals.sort(key=lambda x: x[0])
        non_overlapping = intervals[0]
        removal_count   = 0

        for idx in range(1, len(intervals)):
            start, end = intervals[idx]
            
            if start < non_overlapping[1]:
                # overlapping, need to remove
                non_overlapping[1] = min(non_overlapping[1], end)
                removal_count += 1
            else:
                non_overlapping =  intervals[idx]
                
        return removal_count
'''

# Kunal Wadhwa


'''