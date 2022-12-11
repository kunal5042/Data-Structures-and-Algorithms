# Question: https://leetcode.com/problems/recover-binary-search-tree/
# Medium
from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # O(n) time and O(n) space
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        traversal = []
        stack = []
        node = root
        
        while True:
            while node is not None:
                stack.append(node)
                node = node.left

            if len(stack) == 0: break
            
            node = stack.pop()
            traversal.append(node.val)

            node = node.right
            
        traversal.sort(reverse=True)
        
        def inorder(root):
            if root is None: return
            inorder(root.left)
            root.val = traversal.pop()
            inorder(root.right)
            
        inorder(root)
        return
            


# November 22, 2022

'''

# Kunal Wadhwa

'''