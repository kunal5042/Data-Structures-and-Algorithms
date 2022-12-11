# Question: https://leetcode.com/problems/increasing-order-search-tree/
# Easy
from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # O(n) time and O(h) space
    def increasingBST(self, root: TreeNode) -> TreeNode:
        prev = TreeNode(-1)
        cache = prev
        
        def inorder(node):
            nonlocal prev
            if node is None: return
            inorder(node.left)
        
            node.left = None
            prev.right = node
            prev = node
            
            inorder(node.right)
        
        inorder(root)
        return cache.right
'''

# Kunal Wadhwa

'''