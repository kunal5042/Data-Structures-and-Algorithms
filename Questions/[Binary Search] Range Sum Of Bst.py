# Question: https://leetcode.com/problems/range-sum-of-bst/
# Easy
from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    # O(n) Time
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        _sum = 0
        def helper(node):
            if node is None: return
            # quick-escape
            if node.val  > high and node.left  is None: return
            if node.val  < low  and node.right is None: return 
            
            nonlocal _sum
            
            # update
            if node.val >= low and node.val <= high:
                _sum += node.val
                
            helper(node.left)
            helper(node.right)
                    
            return _sum
        
        return helper(root)
'''

# Kunal Wadhwa

'''