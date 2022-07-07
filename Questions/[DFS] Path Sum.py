# Question: https://leetcode.com/problems/path-sum/

from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None: return False
        
        # DFS Solution
        def helper(node, target, running_sum):
            if node is None: return False
            
            if node.left is None and node.right is None:
                if running_sum + node.val == target: return True
                return False
            
            return helper(node.left, target, running_sum + node.val) \
                or helper(node.right, target, running_sum + node.val)
        
        
        return helper(root, targetSum, 0)

# Kunal Wadhwa
