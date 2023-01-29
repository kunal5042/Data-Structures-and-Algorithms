# Question: https://leetcode.com/problems/maximum-sum-of-an-hourglass/
# Medium
from typing import Optional, List

class Solution:
    # O(m*n) time and O(1) space
    def maxSum(self, grid: List[List[int]]) -> int:
        max_hourglass = 0
        ROWS, COLS = len(grid), len(grid[0])
        
        directions = [(1, 0), (-1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]
        inbounds = lambda x, y: 0 <= x < ROWS and 0 <= y < COLS
        
        for row in range(ROWS):
            for col in range(COLS):
                _sum = grid[row][col]
                hourglass = True

                for x, y in directions:
                    if not inbounds(row + x, col + y):
                        hourglass = False
                        break
                    _sum += grid[row + x][col + y]
                    
                if not hourglass: continue
                max_hourglass = max(max_hourglass, _sum)
                
        return max_hourglass


# January 29, 2023

'''

# Kunal Wadhwa

'''