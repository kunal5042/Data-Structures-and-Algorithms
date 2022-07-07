# Question: https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        return self.construct(deque(preorder), inorder, 0, len(inorder))
    
    
    def construct(self, preorder, inorder, start, end):
        if start > end or len(preorder) <= 0: return None
        
        node = preorder.popleft()
        root = TreeNode(node)
        
        inorder_index = self.get_index_of(inorder, node, start, end)
        
        if inorder_index == -1:
            print('not found')
            return
        
        root.left  = self.construct(preorder, inorder, start, inorder_index-1)
        root.right = self.construct(preorder, inorder, inorder_index+1, end)
        
        return root
        
    
    def get_index_of(self, array, val, start_idx, end_idx):
        for idx in range(start_idx, end_idx+1):
            if array[idx] == val:
                return idx
            
        return -1
'''

# Kunal Wadhwa

# GitHub     : https://github.com/kunal5042
# LeetCode   : https://leetcode.com/kunal5042/
# HackerRank : https://www.hackerrank.com/kunalwadhwa_cs
# LinkedIn   : https://www.linkedin.com/in/kunal5042/

'''