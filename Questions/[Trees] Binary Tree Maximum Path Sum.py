# Question: https://leetcode.com/problems/binary-tree-maximum-path-sum/description/
# Hard
from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # O(n) time and O(n) space
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_path = float('-inf')

        def gain_from_subtree(node):
            if node is None:
                return 0

            # post-order
            gain_from_left  = max(gain_from_subtree(node.left), 0)
            gain_from_right = max(gain_from_subtree(node.right), 0)

            # current node is root to left and right subtree
            # and path forks at this node/root 
            nonlocal max_path
            max_path = max(max_path, gain_from_left + gain_from_right + node.val)

            # return maximum gain this node can provide to the root above
            return max(
                gain_from_left  + node.val,
                gain_from_right + node.val
            )
        
        gain_from_subtree(root)
        return max_path



# December 11, 2022

'''

# Kunal Wadhwa

'''