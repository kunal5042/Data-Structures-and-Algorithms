# Question: https://leetcode.com/problems/shortest-path-in-binary-matrix/description/
# Medium

from collections import deque
from typing import List

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1 or grid[~0][~0] == 1: return -1
        HEIGHT, WIDTH = len(grid), len(grid[0])
        visited = set()
        queue = deque()
        queue.append((0,0))
        distance = 1
        while len(queue):
            count = len(queue)
            for _ in range(count):
                x1, y1 = queue.popleft()
                if (x1, y1) in visited: continue
                visited.add((x1, y1))
                if x1 == HEIGHT-1 and y1 == WIDTH-1:
                    return distance
                for x2, y2 in [(-1, 1), (1, -1), (0, 1), (1, 0),
                    (-1, -1), (1, 1), (-1, 0), (0, -1)]:
                    x3 = x1 + x2
                    y3 = y1 + y2
                    if x3 < 0 or x3 >= HEIGHT: continue
                    if y3 < 0 or y3 >=  WIDTH: continue
                    if (x3, y3) in visited  : continue
                    if grid[x3][y3] == 0:
                        queue.append((x3, y3))
            distance += 1
        return -1
                


# June 01, 2023

'''

# Kunal Wadhwa

'''