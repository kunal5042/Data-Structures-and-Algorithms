# Question: https://leetcode.com/problems/longest-zigzag-path-in-a-binary-tree/
# Medium

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional

class Solution:
    # O(n) time and O(n) space
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        if root is None: return 0        
        longest = [0]
        
        def helper(node, direction, length):
            longest[0] = max(longest[0], length)
            
            # go in opposite direction
            if direction == 'left' and node.right:
                helper(node.right, 'right', length+1)
                helper(node.left, 'left', 1)
            
            if direction == 'right' and node.left:
                helper(node.left, 'left', length+1)
                helper(node.right, 'right', 1)
            
        if root.left:
            helper(root.left, 'left', 1)
            
        if root.right:
            helper(root.right, 'right', 1)
            
        return longest[0]



# April 19, 2023

'''

# Kunal Wadhwa

'''