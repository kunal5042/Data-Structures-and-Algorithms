# Question: https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/description/
# Medium
from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # O(n) time and O(h) space
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        max_diff = [float('-inf')]

        def helper(node):
            if node is None:
                return float('inf'), float('-inf')

            x1, y1 = helper(node.left)
            x2, y2 = helper(node.right)

            _min = min(x1, x2, node.val)
            _max = max(y1, y2, node.val)

            d1 = abs(node.val - _min)
            d2 = abs(node.val - _max)
            d3 = max_diff[0]

            max_diff[0] = max(d1, d2, d3)

            return _min, _max

        helper(root)
        return max_diff[0]


# December 09, 2022

'''

# Kunal Wadhwa

'''