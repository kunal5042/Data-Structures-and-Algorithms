# Question: https://leetcode.com/problems/number-of-islands/
# Medium
from typing import Optional, List
from collections import deque
class Islands_BFS:
    def __init__(self, grid):
        self.width  = len(grid[0])
        self.height = len(grid)
        self.g      = grid
        self.islands_found = 0
        self.islands()
        
    def is_valid(self, coordinates):
        row, col = coordinates
        if row < 0 or row >= self.height: return False
        if col < 0 or col >= self.width : return False
        return True
        
    def adjacents(self, x, y):
        directions = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
        result     = list()
        for dir in directions:
            if self.is_valid(dir):
                result.append(dir)
        
        return result
    
    def bfs(self, idx, jdx, visited):
        q = deque()
        q.append((idx, jdx))
        while len(q):
            (idx, jdx) = q.popleft()
            visited[(idx, jdx)] = True
            
            for adj in self.adjacents(idx, jdx):
                x1, y1 = adj
                if (x1, y1) not in visited and self.g[x1][y1] == "1":
                    q.append(adj)
                    
        self.islands_found += 1
        
    def islands(self):
        visited = dict()
        for idx in range(self.height):
            for jdx in range(self.width):
                if (idx,jdx) not in visited and self.g[idx][jdx] == "1":
                    self.bfs(idx, jdx, visited)
                    

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        return Islands_BFS(grid).islands_found
'''

# Kunal Wadhwa


'''