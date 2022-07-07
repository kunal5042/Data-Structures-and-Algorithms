# Question: https://leetcode.com/problems/validate-binary-search-tree/

from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.helper(root, float('-inf'), float('inf'))
    
    
    def helper(self, root, lower_bound, upper_bound):
        if root is None:
            return True
        
        if root.val <= lower_bound or root.val >= upper_bound:
            return False
        
        
        # this node is valid
        # if it's left subtree and right subtree are also valid
        # we can say the entire tree starting from this root is a valid BST
        
        is_left_subtree_valid = self.helper(root.left, lower_bound, root.val)
        is_right_subtree_valid = self.helper(root.right, root.val, upper_bound)
        
        return is_left_subtree_valid and is_right_subtree_valid
        
'''

# Kunal Wadhwa

# GitHub     : https://github.com/kunal5042
# LeetCode   : https://leetcode.com/kunal5042/
# HackerRank : https://www.hackerrank.com/kunalwadhwa_cs
# LinkedIn   : https://www.linkedin.com/in/kunal5042/

'''