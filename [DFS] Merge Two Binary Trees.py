# Question: https://leetcode.com/problems/merge-two-binary-trees/
from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if root1 is None and root2 is None: return root1
        if root1 is None and root2 is not None: return root2
        if root2 is None and root1 is not None: return root1
        
        # DFS Solution
        def helper(node1, node2, merged):
            if not node1 and not node2: return merged
            
            if node1 and node2:
                merged     = TreeNode()
                merged.val += node1.val if node1 else 0
                merged.val += node2.val if node2 else 0
                
            else:
                if node1: merged = TreeNode(node1.val)
                if node2: merged = TreeNode(node2.val)
            
            merged.left  = helper(node1.left  if node1 else None, node2.left  if node2 else None, None)
            merged.right = helper(node1.right if node1 else None, node2.right if node2 else None, None)
            
            return merged

        # call helper
        return helper(root1, root2, TreeNode())
    
# Kunal Wadhwa
