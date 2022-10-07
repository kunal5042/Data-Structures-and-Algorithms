# Question: https://leetcode.com/problems/time-based-key-value-store/
# Medium
from typing import Optional, List
from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.container = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.container[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.container or len(self.container[key]) == 0:
            return ''
        
        # binary-search
        # because timestamps are always going to be in sorted order
        start, end = 0, len(self.container[key])-1
        while start <= end:
            middle = (start + end) // 2
            if self.container[key][middle][0] == timestamp:
                return self.container[key][middle][1]
            
            if self.container[key][middle][0] < timestamp:
                start = middle + 1
            else:
                end = middle -1

        # if we didn't find the timestamp
        # return value of previous timestamp, if no previous timestamp exists
        # then, return an empty string
        return self.container[key][start-1][1] if start != 0 else ''
'''

# Kunal Wadhwa

'''