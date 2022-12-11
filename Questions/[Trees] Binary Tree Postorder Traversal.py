# Question: https://leetcode.com/problems/binary-tree-postorder-traversal/
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
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        output = []
        
        def postorder(node):
            if node is None: return
            postorder(node.left)
            postorder(node.right)
            output.append(node.val)
            return output
        
        return postorder(root)
'''

# Kunal Wadhwa

'''