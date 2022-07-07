# Question: https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/

from typing import Optional, List
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None: return list()
        
        q = deque()
        q.append(root)
        
        traversal = list()
        zigzag    = False
        while len(q):
            nodes = len(q)
            level = [None for _ in range(nodes)]
            for idx in range(nodes):
                current_node = q.popleft()

                if current_node.left : q.append(current_node.left)
                if current_node.right: q.append(current_node.right)
                
                if zigzag:
                    level[~idx] = current_node.val
                else:
                    level[idx]  = current_node.val
                
            traversal.append(level)
            zigzag = not zigzag
            
        return traversal

# Kunal Wadhwa
