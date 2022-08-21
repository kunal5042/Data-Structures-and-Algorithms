# Question: https://leetcode.com/problems/word-search/
# Medium
# DFS along with backtracking
from typing import Optional, List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        HEIGHT, WIDTH = len(board), len(board[0])
        found = False

        def get_valid_adjacents(row, col, widx):
            directions = [(+1, 0), (-1, 0), (0, -1), (0, +1)]
            adjacents   = []
            
            for _dir in directions:
                offset_r, offset_c = _dir
                adj_r, adj_c = row + offset_r, col + offset_c
                
                if adj_r < 0 or adj_r >= HEIGHT or adj_c < 0 or adj_c >= WIDTH:
                    continue
                    
                if board[adj_r][adj_c] == word[widx]:
                    adjacents.append((adj_r, adj_c))
                    
            return adjacents
        
        
        def depth_first_match(row, col, widx, visited):
            nonlocal found
            if board[row][col] == word[widx]:
                visited[(row, col)] = True
                widx += 1
                
            if widx == len(word):
                found = True
                return
            
            for adjacent in get_valid_adjacents(row, col, widx):
                if adjacent not in visited:
                    visited[adjacent] = True
                    new_row, new_col = adjacent
                    depth_first_match(new_row, new_col, widx, visited)
                    # backtrack
                    del visited[adjacent]
                    if found:
                        return
                    
        for row in range(HEIGHT):
            for col in range(WIDTH):
                if board[row][col] == word[0]:
                    visited = {}
                    depth_first_match(row, col, 0, visited)
                    if found: return True
                    
        return False
'''

# Kunal Wadhwa


'''