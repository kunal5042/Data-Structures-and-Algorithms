# Question: https://leetcode.com/problems/as-far-from-land-as-possible/
# Medium

from collections import deque
from typing import List

class Solution:
    # Multi-Sourced BFS algorithm
    # O(n*n) time and O(n*n) space
    def maxDistance(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = [[False for _ in range(COLS)] for _ in range(ROWS)]
        
        queue = deque()
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1:
                    queue.append((row, col))
                    
        max_distance = -1
        while len(queue):
            nodes = len(queue)
            
            for _ in range(nodes):
                row, col = queue.popleft()
                
                visited[row][col] = True
                
                for x, y in [(1,0), (-1,0), (0,1), (0,-1)]:
                    arow = row + x
                    acol = col + y
                    
                    if any([arow < 0, acol < 0, arow >= ROWS, acol >= COLS]):
                        continue
                        
                    if grid[arow][acol] == 0 and not visited[arow][acol]:
                        queue.append((arow, acol))
                        visited[arow][acol] = True
                        
            max_distance += 1
            
        return max_distance if max_distance > 0 else -1


# February 10, 2023

'''

# Kunal Wadhwa

'''