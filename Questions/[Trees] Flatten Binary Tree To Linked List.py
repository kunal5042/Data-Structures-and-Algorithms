# Question: https://leetcode.com/problems/flatten-binary-tree-to-linked-list/
# Medium
# To Do: Revisit
from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # O(n) Time and O(1) Space
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root is None: return
        
        buffer = root.right
        root.right = root.left
        root.left = None
        
        current = root
        while current.right is not None:
            current = current.right
            
        current.right = buffer
        
        self.flatten(root.right)
    
    # O(n) Time and O(n) Space
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        traversal = []
        
        def preorder(node):
            if node is None: return

            traversal.append(node)
            preorder(node.left)
            preorder(node.right)
            
        preorder(root)
        
        for idx in range(1, len(traversal)):
            node = traversal[idx]
            prev = traversal[idx-1]
            
            prev.right = node
            prev.left  = None
            
'''

# Kunal Wadhwa

'''