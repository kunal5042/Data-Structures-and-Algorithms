# Question: https://leetcode.com/problems/diameter-of-binary-tree/

from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class TreeInfo:
    def __init__(self):
        self.diameter = 0
        
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None: return 0
        
        tree = TreeInfo()
        
        def get_diameter(node, longest_path_down):
            if node is None:
                return 0
            left             = get_diameter(node.left, longest_path_down)
            right            = get_diameter(node.right, longest_path_down)
            current_diameter = left + right
            
            tree.diameter    = max(tree.diameter, current_diameter)

            return 1 + max(left, right)
        
        get_diameter(root, 0)
        return tree.diameter

# Kunal Wadhwa
