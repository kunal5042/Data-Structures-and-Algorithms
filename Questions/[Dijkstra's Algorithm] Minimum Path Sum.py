# Question: https://leetcode.com/problems/minimum-path-sum/

from typing import Optional, List

from heapq import heappop, heappush, heapify
class Node:
    def __init__(self, row: 'int', col: 'int', val: 'int') -> 'Node':
        self.row = row
        self.col = col
        self.val = val
        self.adjacents = set()
        
    def connect_with(self, node2: 'Node') -> 'None':
        weight = node2.val
        self.adjacents.add((weight, node2))
        
    def __lt__(self, node2: 'Node') -> 'bool':
        return self.val < node2.val
        
class GridToGraph:
    def __init__(self, grid: '[[int], ..]') -> 'GridToGraph':
        self.nodes = {}
        self.HEIGHT = len(grid)
        self.WIDTH  = len(grid[0])
        self.initialize_nodes(grid)
        self.build_graph()
        
    def initialize_nodes(self, grid: '[[int], ..]') -> 'None':
        """Creates a node object for every cell in the grid"""
        for row in range(self.HEIGHT):
            for col in range(self.WIDTH):
                value = grid[row][col]
                coord = (row, col)
                self.nodes[coord] = Node(row, col, value)
    
    def build_graph(self) -> 'Node':
        """Adds edges among nodes"""
        def get_adjacent_nodes(srow: 'int', scol: 'int') -> '[Node]':
            directions = [(1, 0), (0, 1)]
            adjacents  = []
            for off_r, off_c in directions:
                adj_r = srow + off_r
                adj_c = scol + off_c
                if any([adj_r < 0, adj_c < 0]): continue
                if any([adj_r >= self.HEIGHT, adj_c >= self.WIDTH]): continue
                adjacents.append(self.nodes[(adj_r, adj_c)])
            return adjacents
        
        for row in range(self.HEIGHT):
            for col in range(self.WIDTH):
                for adjacent in get_adjacent_nodes(row, col):
                    self.nodes[(row, col)].connect_with(adjacent)
                    
                    
    def get_minimum_path_sum(self, source: '(row, col)', dest: '(row, col)') -> 'int':
        """Returns the sum of the weights of the shortest path from source to dest."""
        explored = set()
        source_node = self.nodes[source]
        unexplored = [(source_node.val, source_node)]
        heapify(unexplored)
        path_sums = [[float('inf') for _ in range(self.WIDTH)] for _ in range(self.HEIGHT)]
        path_sums[source[0]][source[1]] = source_node.val
        
        while len(unexplored) != 0:
            psum, node = heappop(unexplored)
            
            if node in explored: continue
            explored.add(node)
            
            for weight, adj_node in node.adjacents:
                if adj_node in explored: continue
                    
                updated_sum = psum + weight
                if updated_sum < path_sums[adj_node.row][adj_node.col]:
                    path_sums[adj_node.row][adj_node.col] = updated_sum
                    heappush(unexplored, (updated_sum, adj_node))
                    
        return path_sums[dest[0]][dest[1]]
        
class Solution:
    # O((|E| + |V|) * log(V)) Time and O(V + E) Space
    def minPathSum(self, grid: List[List[int]]) -> int:
        graph = GridToGraph(grid)
        return graph.get_minimum_path_sum((0,0), (len(grid)-1, len(grid[0])-1))
'''

# Kunal Wadhwa

'''