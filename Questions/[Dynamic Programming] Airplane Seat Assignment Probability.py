# Question: https://leetcode.com/problems/airplane-seat-assignment-probability/
# Medium
from typing import Optional, List

class Solution:
    # O(1) time and O(1) space
    def nthPersonGetsNthSeat(self, n: int) -> float:
        if n > 2: return 1 / 2
        return 1 / n


# January 01, 2023

'''

# Kunal Wadhwa

'''