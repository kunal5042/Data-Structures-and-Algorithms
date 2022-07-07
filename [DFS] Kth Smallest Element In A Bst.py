# Question: https://leetcode.com/problems/kth-smallest-element-in-a-bst/

from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val: int=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """Given the root of a BST and an integer k indicating
        position in the BST. Returns the kth smallest value in the BST
        Runs in O(h + k) Time
        """
        return self.iterative_inorder(root, k)[~0]
    
    def iterative_inorder(self, root: TreeNode, k: int) -> List[int]:
        """Given the root node and an integer k
        returns inorder-traversal of this tree upto k nodes
        """
        # base-case
        if root is None: return []
        stack = []
        traversal = []
        node  = root
        
        while True:
            while node is not None:
                stack.append(node)
                node = node.left

            if len(stack) == 0: break
            
            node = stack.pop()
            traversal.append(node.val)

            k -= 1
            if k == 0: return traversal

            node = node.right
            
        return traversal
'''

# Kunal Wadhwa

# GitHub     : https://github.com/kunal5042
# LeetCode   : https://leetcode.com/kunal5042/
# HackerRank : https://www.hackerrank.com/kunalwadhwa_cs
# LinkedIn   : https://www.linkedin.com/in/kunal5042/

'''