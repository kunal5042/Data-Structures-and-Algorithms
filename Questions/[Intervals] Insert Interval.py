# Question: https://leetcode.com/problems/insert-interval/
# Medium

from typing import Optional, List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if len(intervals) == 0: return [newInterval]
        
        idx = len(intervals) - 1
        inserted = False
        # insert at correct position
        while intervals[idx][0] > newInterval[0]:
            idx -= 1
            
            # insert at start
            if idx < 0:
                intervals.insert(0, newInterval)
                inserted = True
                break
                
        # insert at end
        if not inserted: intervals.insert(idx+1, newInterval)
            
        result = []
        merged = intervals[0]
        
        # merge
        for idx in range(1, len(intervals)):
            this_interval = intervals[idx]
            
            if this_interval[0] > merged[1]:
                # non-overlap
                result.append(merged)
                merged = this_interval
            else:
                # overlap
                merged[0] = min(merged[0], this_interval[0])
                merged[1] = max(merged[1], this_interval[1])
           
        # edge case
        if len(result) == 0: result.append(merged)
        if result[~0] != merged: result.append(merged)
        
        return result
'''

# Kunal Wadhwa

'''