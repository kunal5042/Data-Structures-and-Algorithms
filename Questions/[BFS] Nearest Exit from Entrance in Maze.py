# Question: https://leetcode.com/problems/nearest-exit-from-entrance-in-maze/
# Medium
from typing import Optional, List
from collections import deque
class Solution:
    # O(m*n) time and O(max(m, n)) space
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        visited = set()
        shortest_path = float('inf')
        
        HEIGHT = len(maze)
        WIDTH  = len(maze[0])
        
        is_border  = lambda x, y: any([x == 0, y == 0, x == HEIGHT-1, y == WIDTH-1])
        in_bounds = lambda x, y: not any([x < 0, y < 0, x >= HEIGHT, y >= WIDTH])

        startrow = entrance[0]
        startcol = entrance[1]
        queue = deque([(0, startrow, startcol)])
        
        
        while len(queue) != 0:
            dist, row, col = queue.popleft()
            
            if (row, col) in visited:
                continue
                
            if is_border(row, col) and not(row == startrow and col == startcol):
                shortest_path = min(shortest_path, dist)
                break

            visited.add((row, col))
            
            for adjr, adjc in [(row+1, col), (row-1, col), (row, col-1), (row, col+1)]:
                if (adjr, adjc) not in visited and in_bounds(adjr, adjc) and maze[adjr][adjc] == '.':
                    queue.append((dist+1, adjr, adjc))
                    
                    
        return shortest_path if shortest_path != float('inf') else -1
            


# November 21, 2022

'''

# Kunal Wadhwa

'''