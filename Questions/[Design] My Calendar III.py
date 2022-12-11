# Question: https://leetcode.com/problems/my-calendar-iii/
# Hard
# To Do: Implement using Segment Tree

from typing import Optional, List
from sortedcontainers import SortedDict

# O(n*n) Time complexity and O(n) Space complexity
class MyCalendarThree:

    def __init__(self):
        self.diff = SortedDict()

    # using Sweep-line Algorithm
    def book(self, start: int, end: int) -> int:
        self.diff[start] = self.diff.get(start, 0) + 1
        self.diff[end] = self.diff.get(end, 0) - 1
        current = result = 0
        for delta in self.diff.values():
            current += delta
            result = max(result, current)
        return result
'''

# Kunal Wadhwa

'''