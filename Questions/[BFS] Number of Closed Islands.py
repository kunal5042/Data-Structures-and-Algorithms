# Question: https://leetcode.com/problems/number-of-closed-islands/
# Medium
from typing import Optional, List

class Solution:
    # O(n*m) time and O(n*m) space
    def closedIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        ROWS, COLS = len(grid), len(grid[0])
        
        def inbounds(row, col):
            if row < 0 or row >= ROWS: return False
            if col < 0 or col >= COLS: return False
            return True
        
        def touches_border(row, col):
            if row == 0 or row == ROWS-1: return True
            if col == 0 or col == COLS-1: return True
            return False
        
        def is_closed_island(srow, scol):
            queue = deque([(srow, scol)])
            closed = True
            while len(queue) != 0:
                row, col = queue.popleft()
                
                if touches_border(row, col) is True:
                    closed = False
                
                if (row, col) in visited: continue
                visited.add((row, col))
                
                for x, y in [(0,1), (0,-1), (1,0), (-1,0)]:
                    arow, acol = row + x, col + y
                    if inbounds(arow, acol) is False: continue
                    if (arow, acol) not in visited and grid[arow][acol] == 0:
                        queue.append((arow, acol))
            return closed
        
        number_of_closed = 0
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 0 and (row, col) not in visited:
                    if is_closed_island(row, col) is True:
                        number_of_closed += 1
        
        return number_of_closed
                    


# January 28, 2023

'''

# Kunal Wadhwa

'''