# Question: https://leetcode.com/problems/shortest-path-in-binary-matrix/
# Medium
# Finding the intuition wasn't that simple
from typing import Optional, List

from heapq import heapify as heap, heappop as pop, heappush as push  
class Node:
    def __init__(self, row: 'int', col: 'int', val: 'int') -> 'Node':
        self.row = row
        self.col = col
        self.val = val
        self.adjacents = set()
        
    def connect(self, node2: 'Node') -> 'None':
        weight = node2.val
        self.adjacents.add((weight, node2))
        
    def __lt__(self, node2: 'Node') -> 'bool':
        return self.val < node2.val
    
class Graph:
    def __init__(self, grid: '[[int], ..]') -> 'Graph':
        self.nodes = {}
        self.HEIGHT = len(grid)
        self.WIDTH  = len(grid[0])
        self.initialize_nodes(grid)
        self.build_graph()
        
    def initialize_nodes(self, grid: '[[int], ..]') -> 'None':
        """Creates a node object for every cell in the grid"""
        for row in range(self.HEIGHT):
            for col in range(self.WIDTH):
                val = grid[row][col]
                self.nodes[(row, col)] = Node(row, col, val)
    
    def build_graph(self) -> 'Node':
        """Adds edges among nodes"""
        def get_adjacents(srow, scol):
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1),
                          (-1, -1), (1, 1), (-1, 1), (1, -1)]
            
            adjacents = []
            for off_r, off_c in directions:
                adj_r = srow + off_r
                adj_c = scol + off_c
                
                if any([adj_r < 0, adj_c < 0, adj_r >= self.HEIGHT, 
                        adj_c >= self.WIDTH]): continue
                adjacents.append((adj_r, adj_c))
                
            return adjacents
        
        for row in range(self.HEIGHT):
            for col in range(self.WIDTH):
                for adj_r, adj_c in get_adjacents(row, col):
                    self.nodes[(row, col)].connect(self.nodes[(adj_r, adj_c)])
        
    
    def shortest_path(self, source: '(row, col)', dest: '(row, col)') -> 'int':
        """Returns the shortest clear path from source to dest"""
        # using Dijkstra's Algorithm
        source_node = self.nodes[(source[0], source[1])]
        if source_node.val == 1: return -1
        
        unexplored = [(1, source_node)]
        heap(unexplored)
        explored = set()

        distances = [[float('inf') for _ in range(self.WIDTH)] for _ in range(self.HEIGHT)]
        distances[source[0]][source[1]] = 1
        
        while len(unexplored) != 0:
            path_sum, node = pop(unexplored)
            
            if node in explored: continue
            explored.add(node)
            
            for _psum, adj_node in node.adjacents:
                if adj_node in explored: continue
                if _psum != 0: continue
                
                new_psum = path_sum + 1
                arow, acol = adj_node.row, adj_node.col
                if new_psum < distances[arow][acol]:
                    distances[arow][acol] = new_psum
                    push(unexplored, (new_psum, adj_node))
                    
        if distances[dest[0]][dest[1]] == float('inf'): return -1
        return distances[dest[0]][dest[1]]
                
class Solution:
    # O((|E| + |V|) * log(V)) Time and O(V + E) Space
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        graph = Graph(grid)
        return graph.shortest_path((0, 0), (len(grid)-1, len(grid[0])-1))
'''

# Kunal Wadhwa

'''