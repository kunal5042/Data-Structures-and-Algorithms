# Question: https://leetcode.com/problems/diagonal-traverse/
# Medium
from typing import Optional, List
from collections import defaultdict

class Solution:
    # O(n*m) time and O(1) space with directional checks
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        traversal = []
        
        HEIGHT, WIDTH = len(mat), len(mat[0])
        row, col = 0, 0
        direction = 'up'
        
        def outbounds(x, y):
            return (
                x >= HEIGHT or y >= WIDTH
                or x < 0 or y < 0
            )
        
        while True:
            if not outbounds(row, col):
                traversal.append(mat[row][col])
                
                if direction == 'down':
                    row += 1
                    col -= 1
                else:
                    row -= 1
                    col += 1
                continue
            
            if direction == 'down':
                row -= 1
                col += 1
            else:
                row += 1
                col -= 1
                
            if direction == 'down':
                if row + 1 < HEIGHT:
                    row += 1
                    
                elif col + 1 < WIDTH:
                    col += 1
                    
                else:
                    break
                    
            else:
                if col + 1 < WIDTH:
                    col += 1
                    
                elif row + 1 < HEIGHT:
                    row += 1
                    
                else:
                    break
                    
            direction = 'up' if direction == 'down' else 'down'
            
        return traversal

    # O(m*n) time and O(m*n) space
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        diagonals = defaultdict(list)
        for row in range(len(mat)):
            for col in range(len(mat[0])):
                diagonals[row+col].append(mat[row][col])
        
        traversal = []
        diagonals = list(diagonals.values())
        for idx in range(len(diagonals)):
            if idx % 2 == 0:
                for val in diagonals[idx][::-1]: traversal.append(val)
                continue
                
            for val in diagonals[idx]: traversal.append(val)
                
        return traversal


# December 17, 2022

'''

# Kunal Wadhwa

'''