# Question: https://leetcode.com/problems/word-search/
# Medium
# DFS along with backtracking
from typing import Optional, List

class Solution:
    # O(n*n) * O(n*n) Time
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

    """I wrote this solution, when I solved it again after 2 months."""
    # O(n*n) * O(n*n) Time
    def exist(self, board: List[List[str]], word: str) -> bool:
        HEIGHT = len(board)
        WIDTH  = len(board[0])
        visited = set()
        
        inbounds = lambda x, y: 0 <= x < HEIGHT and 0 <= y < WIDTH
        
        def depth_first_search(row, col, idx) -> bool:
            visited.add((row, col))

            if idx == len(word):
                return True
            
            adjacent_row = (1, -1, 0, 0)
            adjacent_col = (0, 0, 1, -1)
            
            for offset in range(4):
                arow = row + adjacent_row[offset]
                acol = col + adjacent_col[offset]
                
                if not inbounds(arow, acol) or (arow, acol) in visited:
                    continue
                
                if board[arow][acol] == word[idx]:
                    if depth_first_search(arow, acol, idx+1) is True:
                        return True

            visited.remove((row, col))
            return False
        
        for r in range(HEIGHT):
            for c in range(WIDTH):
                if board[r][c] == word[0]:
                    if depth_first_search(r, c, 1) is True:
                        return True
        
        return False
'''

# Kunal Wadhwa


'''