# Question: https://leetcode.com/problems/minimum-absolute-difference-in-bst/description/
# Easy


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional

class Solution:
    def __init__(self):
        self.min_abs_diff = float('inf')
        self.prev_node = None

    def get_min_inorder(self, node):
        if node is None:
            return -1

        self.get_min_inorder(node.left)

        if self.prev_node is not None:
            self.min_abs_diff = min(
                abs(node.val - self.prev_node.val),
                self.min_abs_diff
            )

        self.prev_node = node
        self.get_min_inorder(node.right)
        return self.min_abs_diff

    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        return self.get_min_inorder(root)
        


# June 14, 2023

'''

# Kunal Wadhwa

'''