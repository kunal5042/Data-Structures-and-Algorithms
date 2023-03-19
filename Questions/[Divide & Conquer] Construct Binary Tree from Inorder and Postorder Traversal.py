# Question: https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/
# Medium

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import List, Optional

class Solution:
    # O(n) time and O(h) space
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        # given that all values are unique, O(1) index lookup
        index_map = {val:idx for idx, val in enumerate(inorder)}
        root_index = [len(inorder)-1]
        
        def reconstruct(left, right):
            # base case
            if left > right: return None
            
            node = TreeNode(postorder[root_index[0]])
            root_index[0] -= 1
            
            # recursively resolve roots
            node.right = reconstruct(index_map[node.val]+1, right)
            node.left  = reconstruct(left, index_map[node.val]-1)
            return node
        
        return reconstruct(0, len(inorder)-1)


# March 19, 2023

'''

# Kunal Wadhwa

'''