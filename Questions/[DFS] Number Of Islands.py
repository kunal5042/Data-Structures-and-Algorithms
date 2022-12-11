# Question: https://leetcode.com/problems/number-of-islands/
# Medium
# Mark all chains, keep track of the count of these chains
from typing import Optional, List
class Islands_DFS:
    def __init__(self, grid):
        self.width  = len(grid[0])
        self.height = len(grid)
        self.g      = grid
        self.visited= dict()
        self.found  = 0
        self.islands()
        
    def dfs(self, row, col):
        if row < 0 or row >= self.height or col < 0 or col >= self.width:
            return
        
        if (row, col) not in self.visited and self.g[row][col] == '1':
            self.visited[(row, col)] = True
            self.dfs(row+1, col)
            self.dfs(row-1, col)
            self.dfs(row, col-1)
            self.dfs(row, col+1)
        
    def islands(self):
        for row in range(self.height):
            for col in range(self.width):
                if (row, col) not in self.visited and self.g[row][col] == "1":
                    self.dfs(row, col)
                    self.found += 1

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        return Islands_DFS(grid).found

'''

# Kunal Wadhwa


'''