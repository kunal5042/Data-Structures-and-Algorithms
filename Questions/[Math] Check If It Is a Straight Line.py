# Question: https://leetcode.com/problems/check-if-it-is-a-straight-line/description/
# Easy

import math
from typing import List

class Solution:
    def get_slope(self, P1, P2):
        x1, y1 = P1
        x2, y2 = P2
        try:
            return (y2 - y1) / (x2 - x1)
        except:
            return math.inf

    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        delta = self.get_slope(coordinates[0], coordinates[1])
        for idx in range(2, len(coordinates)):
            if delta != self.get_slope(coordinates[0], coordinates[idx]):
                return False
        return True



# June 05, 2023

'''

# Kunal Wadhwa

'''