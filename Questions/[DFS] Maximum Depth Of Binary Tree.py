# Question: https://leetcode.com/problems/maximum-depth-of-binary-tree/
# Easy
# 
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None: return 0
        
        # DFS Solution
        def helper(node, depth=0):
            if node is None:
                return depth
            
            return max(depth, helper(node.left, depth+1), helper(node.right, depth+1))
        
        
        return helper(root)
# Kunal Wadhwa
