# Question: https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/
# Medium
# 
from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    # O(n) Time and O(n) Space
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        inorder_index = {val:idx for idx, val in enumerate(inorder)}
        root_idx = len(postorder)-1
        
        def construct(left, right):
            nonlocal root_idx
            if left > right: return None
            root = TreeNode(postorder[root_idx])
            root_idx -= 1
            root.right = construct(inorder_index[root.val]+1, right)
            root.left  = construct(left, inorder_index[root.val]-1 )
            
            return root
        
        return construct(0, len(inorder)-1)
'''

# Kunal Wadhwa

'''