# Question: https://leetcode.com/problems/binary-tree-pruning/
# Medium
from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    # O(n) Time and O(h) Space
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None : return root
        
        def prune(node) -> bool:
            if node is None : return False
            
            left  = prune(node.left)
            right = prune(node.right)
            
            if left  is False: node.left  = None
            if right is False: node.right = None
            
            return node.val == 1 or left or right
        
        if prune(root) is False: return None
        return root
'''

# Kunal Wadhwa

'''