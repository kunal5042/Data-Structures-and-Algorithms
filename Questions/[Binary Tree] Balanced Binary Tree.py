# Question: https://leetcode.com/problems/balanced-binary-tree/

from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        """Given a reference to the root node of a binary tree.
        Checks if the given tree is balanced.
        Returns boolean accordingly
        """
        result = [True]
        
        # bottom-up
        def helper(node):
            if node is None: return 0
            
            left = helper(node.left)
            right = helper(node.right)
 
            if abs(left - right) > 1: result[0] = False
                
            return 1 + max(left, right)
        
        helper(root)
        return result[0]
            	
'''

# Kunal Wadhwa

'''