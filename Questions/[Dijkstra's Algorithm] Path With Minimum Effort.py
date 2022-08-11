# Question: https://leetcode.com/problems/path-with-minimum-effort/

from typing import Optional, List

from heapq import heapify, heappop, heappush
class Node:
    def __init__(self, coordinates, val) -> 'Node':
        row, col = coordinates
        self.row = row
        self.col = col
        self.val = val
        self.adjacents = set()
        
    def connect_with(self, node2) -> None:
        """Connects node2 with self"""
        weight = abs(self.val - node2.val)
        self.adjacents.add((node2, weight))
        
    def __lt__(self, other_node):
        """Compares other_node object with self for priority calculation"""
        return self.val < other_node.val
        
class GridToGraph:
    def __init__(self, grid: List[List[int]]) -> 'GridToGraph':
        self.nodes = {}
        self.HEIGHT = len(grid)
        self.WIDTH  = len(grid[0])
        self.initialize_nodes(grid)
        self.build_graph()
        
    def initialize_nodes(self, grid: List[List[int]]) -> None:
        """Creates a node object for every cell in the grid"""
        for row in range(self.HEIGHT):
            for col in range(self.WIDTH):
                value = grid[row][col]
                coord = (row, col)
                self.nodes[coord] = Node(coord, value)
    
    def build_graph(self) -> None:
        """Adds edges among nodes"""
        def get_adjacent_nodes(srow, scol) -> List[Node]:
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
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
                    
                    
    def shortest_distance_from(self, source: 'Node') -> List[tuple[int, Node]]:
        """ Returns the shortest path from source to all other nodes in an array."""
        distances = [(float('inf'), None) for _ in range(len(self.nodes))]
        distances[(source.row * self.WIDTH) + source.col] = (0, None)
        explored  = set()
        unexplored = [(0, source)]
        heapify(unexplored)

        while len(unexplored) != 0:
            distance, node = heappop(unexplored)

            if node in explored: continue
            explored.add(node)

            for adj_node, adj_distance in node.adjacents:
                if adj_node in explored: continue
                    
                this_path = distance + adj_distance
                adj_node_idx = (adj_node.row * self.WIDTH) + adj_node.col
                
                if this_path < distances[adj_node_idx][0]:
                    distances[adj_node_idx] = (this_path, node)
                    heappush(unexplored, (this_path, adj_node))
             
        return distances

    def get_minimum_effort(self, source: '(row, col)', destination: '(row, col)') -> List[tuple[int, int]] -> int:
        """Returns the minimum effort of the most optimal path from source to destination."""
        source_row, source_col = source
        dest_row, dest_col = destination
        source_node = self.nodes[(source_row, source_col)]
        dest_node = self.nodes[(dest_row, dest_col)]
        
        efforts = [[float('inf') for _ in range(self.WIDTH)] for _ in range(self.HEIGHT)]
        efforts[source_row][source_col] = 0
        
        explored = set()
        unexplored = [(0, source_node)]
        heapify(unexplored)
        
        while len(unexplored) != 0:
            effort, node = heappop(unexplored)
            
            if node in explored: continue
            explored.add(node)
            
            for adj_node, adj_effort in node.adjacents:
                if adj_node in explored: continue
                
                _effort = max(effort, adj_effort)
                
                if _effort < efforts[adj_node.row][adj_node.col]:
                    efforts[adj_node.row][adj_node.col] = _effort
                    heappush(unexplored, (_effort, adj_node))
        
        return efforts[dest_row][dest_col]
                
    def print_shortest_path(self, source: '(row, col)', destination: '(row, col)') -> None:
        """Prints the coordinates of every step of shortest path from source to destination."""
        source_row, source_col = source
        dest_row, dest_col = destination
        source_node = self.nodes[(source_row, source_col)]
        dest_node = self.nodes[(dest_row, dest_col)]
        distances = self.shortest_distance_from_to(source_node, dest_node)
        
        def coordinates_from_id(node_id):
            node_row = node_id % self.HEIGHT
            node_col = node_id // self.WIDTH
            return node_row, node_col
        
        def id_from_coordinates(row, col):
            return (row * self.WIDTH) + col
        
        path = [destination]
        parent = distances[id_from_coordinates(dest_row, dest_col)][1]
        while parent is not None:
            path.append((parent.row, parent.col))
            parent = distances[id_from_coordinates(parent.row, parent.col)][1]
            
        for idx in range(len(path)):
            print(path[~idx])
            
class Solution:
    # O((|HEIGHT * WIDTH| + |E|)* log(HEIGHT * WIDTH)) Time: where E is the number of
    # edges among nodes
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        graph = GridToGraph(heights)
        return graph.get_minimum_effort((0,0), (len(heights)-1, len(heights[0])-1))
'''

# Kunal Wadhwa

'''