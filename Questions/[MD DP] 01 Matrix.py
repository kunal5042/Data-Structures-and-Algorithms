# Question: https://leetcode.com/problems/01-matrix/
# Medium
from typing import Optional, List

class Solution:
    # BFS Solution
    # O(V+E) Time 
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        HEIGHT, WIDTH = len(mat), len(mat[0])
        output = [[float('inf') for _ in range(WIDTH)] for _ in range(HEIGHT)]
        visited = set()
        queue = deque()
        
        # the idea is that, first all the zeroes and their adjacents will be processed
        # and then the adjacent of adjacents will be processed
        # so, we start by exploring all the zeroes
        # thereby ensuring minimum cost updates at the first visit itself
        def expand():
            inbounds = lambda x, y: 0 <= x < HEIGHT and 0 <= y < WIDTH
            
            while len(queue) != 0:
                dist, r, c = queue.popleft()
                visited.add((r,c))
                output[r][c] = min(output[r][c], dist)
                
                for (x,y) in [(r+1,c), (r-1,c), (r,c+1), (r,c-1)]:
                    if inbounds(x,y) and (x,y) not in visited:
                        queue.append((dist+1, x, y))
            return
                
        for row in range(HEIGHT):
            for col in range(WIDTH):
                if mat[row][col] == 0:
                    queue.append((0, row, col))
                
        expand()
        return output
    
    # Multidimensional Dynamic Programming
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        HEIGHT, WIDTH = len(mat), len(mat[0])
        output = mat
        
        for row in range(0, HEIGHT):
            for col in range(0, WIDTH):
                if output[row][col] != 0:
                    top = output[row-1][col] if row > 0 else float('inf')
                    back = output[row][col-1] if col > 0 else float('inf')
                    output[row][col] = min(top, back) + 1
                    
        for row in reversed(range(0, HEIGHT)):
            for col in reversed(range(0, WIDTH)):
                if output[row][col] != 0:
                    down = output[row+1][col] if row+1 < HEIGHT else float('inf')
                    right = output[row][col+1] if col+1 < WIDTH else float('inf')
                    output[row][col] = min(output[row][col], down+1, right+1)

        return output
'''

# Kunal Wadhwa

'''