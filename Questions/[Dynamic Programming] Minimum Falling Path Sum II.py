# Question: https://leetcode.com/problems/minimum-falling-path-sum-ii/
# Hard

from copy import copy
from typing import List

class Solution:
    def getMinExcludingIndex(self, arr, idx):
        result = float('inf')
        for jdx in range(len(arr)):
            if jdx == idx: continue
            result = min(arr[jdx], result)
        return result

    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        HEIGHT, WIDTH = len(grid), len(grid[0])
        paths = [row.copy() for row in grid]

        for rno in range(1, HEIGHT):
            for cno in range(WIDTH):
                paths[rno][cno] += self.getMinExcludingIndex(paths[rno-1], cno)

        return min(paths[~0])


# April 26, 2024

'''

# Kunal Wadhwa

'''