# Question: https://leetcode.com/problems/unique-paths-iii/
# Hard
from typing import Optional, List

class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        HEIGHT, WIDTH = len(grid), len(grid[0])
        start_row, start_col = 0, 0
        empty_cells = 0
        paths = 0
        
        # find the starting position and number of empty cells
        for row in range(HEIGHT):
            for col in range(WIDTH):
                if grid[row][col] == 0: empty_cells += 1
                if grid[row][col] == 1: start_row, start_col = row, col
                
        def dfs_backtrack(row, col, empty):
            if row < 0 or row >= HEIGHT: return
            if col < 0 or col >= WIDTH: return
            if grid[row][col] < 0: return
            
            # reached end from start 
            if grid[row][col] == 2:
                
                # and number of empty cells is zero
                if empty == -1:
                    nonlocal paths
                    paths += 1
                    
                return
            
            # mark as visited
            grid[row][col] = -7
            
            # explore all paths
            for x, y in [(0,1), (0,-1), (1,0), (-1,0)]:
                dfs_backtrack(row + x, col + y, empty - 1)
            
            # unmark
            grid[row][col] = 0
            return
        
        dfs_backtrack(start_row, start_col, empty_cells)
        return paths
                


# December 31, 2022

'''

# Kunal Wadhwa

'''