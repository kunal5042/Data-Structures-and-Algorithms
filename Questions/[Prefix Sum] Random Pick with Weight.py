# Question: https://leetcode.com/problems/random-pick-with-weight/
# Medium
from typing import Optional, List

import random
from bisect import bisect_left
class Solution:

    # O(n + log(n)) time and O(n) space
    def __init__(self, w: List[int]):
        self.weights = w
        for idx in range(1, len(w)):
            self.weights[idx] += self.weights[idx-1]

    def pickIndex(self) -> int:
        return bisect_left(self.weights, random.randint(1, self.weights[~0]))

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()


# January 26, 2023

'''

# Kunal Wadhwa

'''