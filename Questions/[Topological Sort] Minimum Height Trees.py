# Question: https://leetcode.com/problems/minimum-height-trees/

from typing import Optional, List

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n <= 2: return [x for x in range(n)]
        
        neighbors = [set() for node in range(n)]
        for start, end in edges:
            neighbors[start].add(end)
            neighbors[end].add(start)
        
        leaves = []
        for node in range(n):
            if len(neighbors[node]) == 1:
                leaves.append(node)
                
        # Trim leaves until we reach the centroids
        remaining_nodes = n
        while remaining_nodes > 2:
            remaining_nodes -= len(leaves)
            new_leaves = []
            
            while len(leaves) != 0:
                leaf = leaves.pop()
                neighbor = neighbors[leaf].pop()
                neighbors[neighbor].remove(leaf)
                
                if len(neighbors[neighbor]) == 1:
                    new_leaves.append(neighbor)
                    
            leaves = new_leaves
                
        return leaves
    

# Algorithm:
# - Initially, we would build a graph with the adjacency list from the input.

# - We then create a queue which would be used to hold the leaf nodes.

# - At the beginning, we put all the current leaf nodes into the queue.

# - We then run a loop until there is only two nodes left in the graph.

# - At each iteration, we remove the current leaf nodes from the queue. While removing the nodes, we also remove the edges that are linked to the nodes. As a consequence, some of the non-leaf nodes would become leaf nodes. And these are the nodes that would be trimmed out in the next iteration.

# - The iteration terminates when there are no more than two nodes left in the graph, which are the desired centroids nodes.
'''

# Kunal Wadhwa

'''