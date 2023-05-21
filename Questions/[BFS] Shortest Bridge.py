# Question: https://leetcode.com/problems/shortest-bridge/description/
# Medium

from collections import deque
from typing import List

class Solution:
    # O(n*n) time and O(n*n) space
    def shortestBridge(self, grid: List[List[int]]) -> int:
        HEIGHT, WIDTH = len(grid), len(grid[0])

        def is_inbounds(row: int, col: int) -> bool:
            if row < 0 or row >= HEIGHT: return False
            if col < 0 or col >= WIDTH : return False
            return True

        def get_directions(row: int, col: int) -> List[tuple]:
            directions = []
            for off_r, off_c in [(-1,0),(1,0),(0,1),(0,-1)]:
                adj_r = off_r + row
                adj_c = off_c + col
                if not is_inbounds(adj_r, adj_c): continue
                directions.append((adj_r, adj_c))
            return directions

        def get_chain(row: int, col: int) -> set:
            chain = set()

            def build_chain(source_row: int, source_col: int) -> None:
                grid[source_row][source_col] = 2
                chain.add((source_row, source_col))
                for adj_row, adj_col in get_directions(source_row, source_col):
                    if grid[adj_row][adj_col] == 1:
                        build_chain(adj_row, adj_col)
            
            build_chain(row, col)
            return chain

        def get_shortest_bridge_to_island_two(island_one: set) -> int:
            queue = deque(island_one)
            distance = 0

            while len(queue) != 0:
                size = len(queue)
                for _ in range(size):
                    row, col = queue.popleft()
                 
                    for adj_row, adj_col in get_directions(row, col):
                        if grid[adj_row][adj_col] ==  0:
                            grid[adj_row][adj_col] = -1
                            queue.append((adj_row, adj_col))
                            
                        if grid[adj_row][adj_col] ==  1:
                            return distance
                
                distance += 1
            return distance

        def get_one_island() -> set:
            for row in range(HEIGHT):
                for col in range(WIDTH):
                    if grid[row][col] == 1:
                        return get_chain(row, col)

        return get_shortest_bridge_to_island_two(get_one_island())


# May 21, 2023

'''

# Kunal Wadhwa

'''