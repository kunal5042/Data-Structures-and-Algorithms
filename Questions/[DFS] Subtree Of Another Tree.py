# Question: https://leetcode.com/problems/subtree-of-another-tree/

from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def same_tree(p, q):
            if p is None and q is not None  : return False
            if q is None and p is not None  : return False
            if p is None and q is None      : return True
            if p.val != q.val               : return False
            
            return True and same_tree(p.left, q.left) and same_tree(p.right, q.right)
        
        def find_potential_nodes(root, sub_root, nodes):
            if root is None:
                return False
            
            if root.val == sub_root.val:
                nodes.append(root)
                
            find_potential_nodes(root.left,  sub_root, nodes)
            find_potential_nodes(root.right, sub_root, nodes)
            
            return nodes
        
        for node in find_potential_nodes(root, subRoot, list()):
            if same_tree(node, subRoot):
                return True
            
        return False

# Kunal Wadhwa
