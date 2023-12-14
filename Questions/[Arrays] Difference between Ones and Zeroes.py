# Question: https://leetcode.com/problems/difference-between-ones-and-zeros-in-row-and-column/description/
# Medium

from copy import copy
from typing import List

class Solution:
    # O(n*m) time and O(n*m) space
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        ones_row = [0 for _ in range(len(grid))]
        ones_col = [0 for _ in range(len(grid[0]))]
        zeroes_row = ones_row.copy()
        zeroes_col = ones_col.copy()
        
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == 1:
                    ones_col[col] += 1
                    ones_row[row] += 1
                else:
                    zeroes_col[col] += 1
                    zeroes_row[row] += 1
        
        diff_matrix = grid.copy()
        for row in range(len(diff_matrix)):
            for col in range(len(diff_matrix[row])):
                diff_matrix[row][col] = ones_col[col] + ones_row[row] - zeroes_row[row] - zeroes_col[col]
        
        return diff_matrix


# December 14, 2023

'''

# Kunal Wadhwa

'''