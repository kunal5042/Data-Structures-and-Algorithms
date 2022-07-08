# Question: https://leetcode.com/problems/merge-intervals/

from typing import Optional, List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result = []
        intervals.sort(key=lambda x:x[0])
        merged = intervals[0]
        
        for idx in range(1, len(intervals)):
            cstart, cend = intervals[idx]
            
            if cstart <= merged[1]:
                # overlapping
                merged[0] = min(merged[0], intervals[idx][0])
                merged[1] = max(merged[1], intervals[idx][1])
                
            else:
                result.append(merged)
                merged = intervals[idx]
           
        if len(result) == 0     : result.append(merged)
        if result[~0] != merged : result.append(merged)

        return result

'''

# Kunal Wadhwa


'''