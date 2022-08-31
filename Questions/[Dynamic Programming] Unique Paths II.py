# Question: https://leetcode.com/problems/unique-paths-ii/
# Medium
#
from typing import Optional, List

class Solution:
    # O(m*n) Time and O(m*n) Space
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1: return 0
        
        HEIGHT, WIDTH = len(grid), len(grid[0])
        ways = [[0 for _ in range(WIDTH)] for _ in range(HEIGHT)]
        ways[0][0] = 1
        
        for col in range(1, WIDTH):
            if grid[0][col] != 1:
                ways[0][col] = ways[0][col-1]
                
        for row in range(1, HEIGHT):
            if grid[row][0] != 1:
                ways[row][0] = ways[row-1][0]
                
        for row in range(1, HEIGHT):
            for col in range(1, WIDTH):
                if grid[row][col] == 1: continue
                    
                ways[row][col] += (ways[row][col-1] + ways[row-1][col])
                
        return ways[~0][~0]
'''

# Kunal Wadhwa

'''