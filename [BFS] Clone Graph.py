# Question: https://leetcode.com/problems/clone-graph/

from typing import Optional, List
from collections import deque

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node                : return None
        if len(node.neighbors) == 0: return Node(node.val)
        
        hashmap = dict()
        
        q = deque()
        q.append(node)
        
        visited = set()
        
        while len(q):
            current = q.popleft()
            if current in visited: continue
                
            visited.add(current)
            
            copy = Node(current.val)
            hashmap[current] = copy
            
            for connected_node in current.neighbors:
                q.append(connected_node)
                
        visited.clear()
        q.append(node)
        
        while len(q):
            current = q.popleft()
            if current in visited: continue
                
            copy    = hashmap[current]
            
            for connected_node in current.neighbors:
                copy.neighbors.append(hashmap[connected_node])
                q.append(connected_node)
                
            visited.add(current)
            
        return hashmap[node]

# Kunal Wadhwa
