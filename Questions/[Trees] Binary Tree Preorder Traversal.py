# Question: https://leetcode.com/problems/binary-tree-preorder-traversal/
# Easy
from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # O(n) Time and O(h) Space
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        output = []
        
        def preorder(root):
            if root is None: return
            output.append(root.val)
            preorder(root.left)
            preorder(root.right)
            return output
        
        return preorder(root)
'''

# Kunal Wadhwa

'''