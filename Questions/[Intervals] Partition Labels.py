# Question: https://leetcode.com/problems/partition-labels/
# Medium
from typing import Optional, List

class Solution:
    # O(n) Time and O(n) Space
    
    def partitionLabels(self, s: str) -> List[int]:
        def merge_overlapping(intervals) -> List[tuple]:
            """Merges overlapping intervals.
            Returns a new list of non-overlapping intervals.
            """
            result = []
            merged = intervals[0]
            for idx in range(1, len(intervals)):
                # over-lap
                if merged[1] >= intervals[idx][0]:
                    merged[0] = min(merged[0], intervals[idx][0])
                    merged[1] = max(merged[1], intervals[idx][1])
                else:
                    result.append(merged)
                    merged = intervals[idx]
                    
            if len(result) == 0: result.append(merged)
            if result[~0] != merged: result.append(merged)
                
            return result
            
        # storing first and last occurence of each character
        _hash = {}
        for idx, char in enumerate(s):
            if char in _hash:
                first, _ = _hash[char]
                _hash[char] = [first, idx]
                
            else:
                _hash[char] = [idx, idx]
        
        intervals = list(_hash.values())
        
        # calculating size of partitions from start and end index
        return [(last - first + 1) for first, last in merge_overlapping(intervals)]
        
'''

# Kunal Wadhwa

'''