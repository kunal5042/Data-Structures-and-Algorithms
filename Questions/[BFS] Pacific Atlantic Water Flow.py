# Question: https://leetcode.com/problems/pacific-atlantic-water-flow/

from typing import Optional, List

from collections import deque
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific_flow, atlantic_flow = set(), set()
        HEIGHT, WIDTH = len(heights), len(heights[0])
        
        def inbounds(row: int, col: int) -> bool:
            if any([row<0, col<0, row>=HEIGHT, col>=WIDTH]):
                return False
            return True
        
        def expand(row: int, col: int) -> List[tuple]:
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            flow_from = []
            for offset_r, offset_c in directions:
                r, c = row + offset_r, col + offset_c
                
                # water can flow from this island to current island
                if inbounds(r, c) and heights[r][c] >= heights[row][col]:
                    flow_from.append((r, c))
                    
            return flow_from
                    
        
        def add_valid_islands(row: int, col:int, flow: set) -> None:
            queue = deque([(row, col)])
            visited = set()
            
            while len(queue):
                row, col = queue.pop()
                if (row, col) in visited: continue
                visited.add((row, col))
                flow.add((row, col))
                for next_island in expand(row, col):
                    queue.append(next_island)
        
        # backtrack to the island from which rain water 
        # can flow to pacific and atlantic
        # from both routes
        
        # route-1
        for col in range(WIDTH):
            add_valid_islands(0, col, pacific_flow)
            add_valid_islands(HEIGHT-1, col, atlantic_flow)
            
        # route-2
        for row in range(HEIGHT):
            add_valid_islands(row, 0, pacific_flow)
            add_valid_islands(row, WIDTH-1, atlantic_flow)
            
        # intersection
        return list(pacific_flow.intersection(atlantic_flow))
'''

# Kunal Wadhwa

'''