# Question: https://leetcode.com/problems/equal-row-and-column-pairs/
# Medium
# Convert into strings
from typing import Optional, List

class Solution:
    # O(n^2) Time and O(n^2) Space
    def equalPairs(self, grid: List[List[int]]) -> int:
        rows, cols = {}, {}
        
        for row in grid:
            str_row = " ".join([str(ele) for ele in row])
            rows[str_row] = rows.get(str_row, 0) + 1
            
        pairs = 0
            
        for col in range(len(grid[0])):
            str_col = ""
            for row in range(len(grid)):
                if row == len(grid) - 1:
                    str_col += str(grid[row][col])
                else:
                    str_col += str(grid[row][col]) + " "
            
            if str_col in rows: pairs += rows[str_col]
            
        return pairs
'''

# Kunal Wadhwa

'''