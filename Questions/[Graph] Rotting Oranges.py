# Question: https://leetcode.com/problems/rotting-oranges/

from typing import Optional, List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        HEIGHT, WIDTH = len(grid), len(grid[0])
        
        def can_rot(row, col) -> List[tuple[int]]:
            """Checks if a fresh tomato can be rotten"""
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            all_empty  = True
            for adjacent in directions:
                adj_r = row + adjacent[0]
                adj_c = col + adjacent[1]
                
                # out of bounds
                if any([adj_r < 0, adj_r >= HEIGHT, adj_c < 0, adj_c >= WIDTH]):
                    continue
                    
                # empty cell
                if grid[adj_r][adj_c] != 0:
                    all_empty = False
                   
            # if all adjacents are empty return False i.e cannot rot
            # if all_empty is False return True i.e we can rot it
            return not all_empty
        
        def get_neighbors(row, col) -> List[tuple[int]]:
            """Returns a neighboring cells of the cell with coordinates row and col in a list"""
            neighbors = []
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            for adjacent in directions:
                adj_r = row + adjacent[0]
                adj_c = col + adjacent[1]
                
                if any([adj_r < 0, adj_r >= HEIGHT, adj_c < 0, adj_c >= WIDTH]):
                    continue
                    
                if grid[adj_r][adj_c] == 1:
                    neighbors.append((adj_r, adj_c))
                   
            return neighbors
            
        def at_least_one_rotten() -> bool:
            """Checks if at least one rotten tomato is present in the grid"""
            for row in range(HEIGHT):
                for col in range(WIDTH):
                    if grid[row][col] == 2:
                        return True
            return False
        
        def at_least_one_fresh_tomato() -> bool:
            """Checks if at least one fresh tomato is present in the grid"""
            for row in range(HEIGHT):
                for col in range(WIDTH):
                    if grid[row][col] == 1:
                        return True
            return False
        
        # there are no rotten tomatoes to rot other fresh tomatoes
        # and there exist at least one fresh tomato, hence -1
        if not at_least_one_rotten() and at_least_one_fresh_tomato(): return -1
        
        minutes_passed = 0
        visited  = set()
        
        while True:
            # rotten tomatoes
            will_rot_others = []
            
            for row in range(HEIGHT):
                for col in range(WIDTH):
                    # fresh tomato, and cannot be rotten
                    if grid[row][col] == 1 and not can_rot(row, col):
                        return -1
                    
                    # rotten tomato and previously not visited
                    if grid[row][col] == 2 and (row, col) not in visited:
                        will_rot_others.append((row, col))
                    
            # if rotten tomatoes are empty
            if len(will_rot_others) == 0:
                # if there exist a fresh tomato
                if at_least_one_fresh_tomato():
                    return -1
                
                # otherwise, return the time it took to rot all tomatoes
                return minutes_passed - 1 if minutes_passed != 0 else 0
                    
                
            # rot the neighboring tomatoes
            while len(will_rot_others) != 0:
                rotten_row, rotten_col = will_rot_others.pop()
                for adj_r, adj_c in get_neighbors(rotten_row, rotten_col):
                    grid[adj_r][adj_c] = 2
                visited.add((rotten_row, rotten_col))
                
            # update
            minutes_passed += 1
'''

# Kunal Wadhwa

'''