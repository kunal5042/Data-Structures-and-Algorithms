# Question: https://leetcode.com/problems/flood-fill/

from typing import Optional, List

from collections import deque
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if color == image[sr][sc]: return image
        
        visited  = set()
        source_color = image[sr][sc]
        
        def get_valid(row, col) -> List[tuple]:
            """Takes two integer representing row and col number in the grid
            Returns a list of tuples representing row and col numbers we can move to
            from the given row and col if they are not out of bounds and not yet have 
            been visited
            """
            nonlocal visited
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            valid = []
            for move_r, move_c in directions:
                new_r, new_c = row + move_r, col + move_c
                
                if any([new_r < 0, new_r >= len(image), new_c < 0, new_c >= len(image[0])]) \
                or (new_r, new_c) in visited:
                    continue
                else:
                    valid.append((new_r, new_c))
            return valid
        
        
        def breadth_first_search(srow, scol) -> None:
            """Performs breadth first search from the given start row and start col.
            And performs color modifications on the cells which meet the criteria.
            """
            nonlocal visited
            queue = deque()
            queue.append((srow, scol))
            
            while len(queue) != 0:
                row, col = queue.popleft()
                
                if (row, col) in visited:
                    continue
                visited.add((row, col))
                    
                if image[row][col] != source_color:
                    continue
                    
                image[row][col] = color
                
                for direction in get_valid(row, col):
                    queue.append(direction)
                    
                    
        breadth_first_search(sr, sc)
        return image
'''

# Kunal Wadhwa

'''