# Question: https://leetcode.com/problems/binary-tree-level-order-traversal/
# Medium
# Literally BFS Implementation
from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None: return list()
        
        q = deque()
        q.append(root)
        
        traversal = list()
        
        while len(q):
            nodes = len(q)
            level = list()
            for _ in range(nodes):
                current_node = q.popleft()
                
                if current_node.left: q.append(current_node.left)
                if current_node.right: q.append(current_node.right)
                    
                level.append(current_node.val)
                
            traversal.append(level)
            
        return traversal

# Kunal Wadhwa
