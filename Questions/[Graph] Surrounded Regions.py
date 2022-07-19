# Question: https://leetcode.com/problems/surrounded-regions/

from typing import Optional, List

from collections import deque
class Trail:
    def __init__(self, srow, scol):
        self.srow = srow
        self.scol = scol
        self.touches_border = False
        self.trail_coordinates = [(srow, scol)]
        
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        HEIGHT, WIDTH = len(board), len(board[0])
        visited = set()
        
        def is_valid_coordinate(row, col):
            """Checks if a coordinate is not out of bounds
            Returns boolean
            """
            if any([row < 0, col < 0, row >= HEIGHT, col >= WIDTH]):
                return False
            return True
        
        def get_adjacents(srow, scol):
            """Takes start row and start col
            Returns all the four vertical and horizontal adjacent coordinates in a list
            """
            directions = [(0,1), (0, -1), (-1, 0), (1, 0)]
            adjacents  = []
            for shift in directions:
                offset_r, offset_c = shift
                adj_r = srow + offset_r
                adj_c = scol + offset_c
                if is_valid_coordinate(adj_r, adj_c):
                    adjacents.append((adj_r, adj_c))
            return adjacents
        
        def is_touching_border(row, col):
            """Takes a coorindate's row and col
            Checks if the this coordinate touches the border of the board
            Returns boolean
            """
            if any([row == 0, col == 0, row == HEIGHT-1, col == WIDTH-1]):
                return True
            return False
        
        def get_trail_info(trail):
            """Takes a trail object
            Updates the trail_coordinates instance variable
            And touches_border instance variable
            Returns None
            """
            queue = deque()
            queue.append((trail.srow, trail.scol))
            
            while len(queue):
                nrow, ncol = queue.pop()
                if (nrow, ncol) in visited:
                    continue
                    
                if is_touching_border(nrow, ncol):
                    trail.touches_border = True
                    
                for adj_r, adj_c in get_adjacents(nrow, ncol):
                    if board[adj_r][adj_c] == "O":
                        queue.append((adj_r, adj_c))
                        trail.trail_coordinates.append((adj_r, adj_c))
                        
                visited.add((nrow, ncol))
        
        def flip_trail(trail):
            """Takes a trail object
            Flips the enitre trail from 'O' to 'X'
            """
            for row, col in trail.trail_coordinates:
                board[row][col] = "X"
            return
        
        """Finds the trails that needs flipping,
        and then flips them in place
        """
        for row in range(HEIGHT):
            for col in range(WIDTH):
                if board[row][col] == "O" and (row, col) not in visited:
                    this_trail = Trail(row, col)
                    get_trail_info(this_trail)
                    if not this_trail.touches_border:
                        flip_trail(this_trail)
                        
        return

'''

# Kunal Wadhwa

'''