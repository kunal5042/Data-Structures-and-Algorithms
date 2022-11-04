# Question: https://leetcode.com/problems/swim-in-rising-water/
# Hard
from typing import Optional, List

class Solution:
    # O(n^2*logn) Time and O(n*n) Space
    def swimInWater(self, grid: List[List[int]]) -> int:
        visited, heap, output = set(), [(grid[0][0], (0, 0))], 0
        H, W = len(grid), len(grid[0])
        
        while len(heap) != 0:
            time, (row, col) = heappop(heap)
            visited.add((row, col))
            
            output = max(output, time)
            
            if row == H-1 and col == W-1:
                return output
            
            for ax, ay in [(row+1, col), (row-1, col), (row, col+1), (row, col-1)]:
                if 0 <= ax < H and 0 <= ay < W and (ax, ay) not in visited:
                    heappush(heap, (grid[ax][ay], (ax, ay)))
                    
        return -1
'''

# Kunal Wadhwa

'''