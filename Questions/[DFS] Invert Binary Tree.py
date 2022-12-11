# Question: https://leetcode.com/problems/invert-binary-tree/
# Easy
# root.left, root.right = root.right, root.left (Recursively)
from collections import deque
from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        return self.reverse(root)
    
    # DFS Solution
    def reverse(self, root):
        if root is None:
            return
        
        root.left, root.right = root.right, root.left
        
        # this node has been reversed
        # now we reverse it's children recursively 
        
        self.reverse(root.left)
        self.reverse(root.right)
        
        return root

# Kunal Wadhwa
