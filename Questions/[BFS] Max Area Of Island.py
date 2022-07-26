# Question: https://leetcode.com/problems/max-area-of-island/

from typing import Optional, List

from collections import deque
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        marked, HEIGHT, WIDTH = set(), len(grid), len(grid[0])
        
        is_island  = lambda row, col: grid[row][col] == 1
        new_island = lambda row, col: (row, col) not in marked
        
        def is_inbounds(row: int, col: int) -> bool:
            if any([row <0, col <0, row >= HEIGHT, col >= WIDTH]):
                return False
            return True
        
        def expand(row: int, col: int, queue: deque) -> None:
            directions = [(0, 1), (-1, 0), (1, 0), (0, -1)]
            for offset_r, offset_c in directions:
                r, c = row + offset_r, col + offset_c
                if not is_inbounds(r, c): continue
                if is_island(r, c) and (r, c) not in marked:
                    queue.append((r, c))
                
            return
        
        def get_island_length(row: int, col: int) -> int:
            queue = deque([(row, col)])
            island_length = 0
            
            while len(queue):
                row, col = queue.pop()
                if (row, col) in marked: continue
                island_length += 1
                marked.add((row, col))
                expand(row, col, queue)
                
            return island_length
        
        def max_area_of_island() -> int:
            largest_island = 0
            for row in range(HEIGHT):
                for col in range(WIDTH):
                    if is_island(row, col) and new_island(row, col):
                        largest_island = max(largest_island, \
                                             get_island_length(row, col))
                        
            return largest_island
        
        
        return max_area_of_island()
'''

# Kunal Wadhwa

'''