# Question: https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/
# Medium
from typing import Optional, List

class Solution:
    # O(n) time and O(n) space
    def removeStones(self, stones: List[List[int]]) -> int:
        islands = 0
        points = set()
        rows, cols = defaultdict(list), defaultdict(list)
        
        for x, y in stones:
            rows[x].append(y)
            cols[y].append(x)
            points.add((x,y))
            
        def remove_connected(row, col):
            if (row, col) in points:
                points.discard((row, col))
                
            for x in cols[col]:
                if (x, col) in points:
                    remove_connected(x, col)
                
            for y in rows[row]:
                if (row, y) in points:
                    remove_connected(row, y)
                
        for px, py in stones:
            if (px, py) in points:
                remove_connected(px, py)
                islands += 1
            
        return len(stones) - islands
'''

# Kunal Wadhwa

'''