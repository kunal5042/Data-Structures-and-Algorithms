# Question: https://leetcode.com/problems/count-good-nodes-in-binary-tree/
# Medium
from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    # O(n) Time and O(h) Space
    def goodNodes(self, root: TreeNode) -> int:
        return self.find_gnodes(root, root.val)
        
    def find_gnodes(self, node, maximum):
        if node is None:
            return 0
        
        result = 0
        if maximum <= node.val:
            result  += 1
            maximum  = node.val
        
        return result + self.find_gnodes(node.left, maximum) + self.find_gnodes(node.right, maximum)
'''

# Kunal Wadhwa

'''