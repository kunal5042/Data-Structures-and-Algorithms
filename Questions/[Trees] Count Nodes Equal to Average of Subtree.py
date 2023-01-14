# Question: https://leetcode.com/problems/count-nodes-equal-to-average-of-subtree/
# Medium
from typing import Optional, List

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # O(n) time and O(h) space
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        result = 0
        def helper(node):
            nonlocal result
            if node is None: return (0, 0)
            lsum, lnodes = helper(node.left)
            rsum, rnodes = helper(node.right)
            avg = (lsum + rsum + node.val) // (lnodes + rnodes + 1)
            if avg == node.val: result += 1
            return (lsum + rsum + node.val, lnodes + rnodes + 1)
        helper(root)
        return result	


# January 14, 2023

'''

# Kunal Wadhwa

'''