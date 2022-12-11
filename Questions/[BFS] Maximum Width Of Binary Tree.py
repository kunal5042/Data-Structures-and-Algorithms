# Question: https://leetcode.com/problems/maximum-width-of-binary-tree/
# Medium
from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        q = deque()
        q.append((root, 0))
        width = 0
        
        while len(q) != 0:
            count = len(q)
            nodes = list()
            
            for _ in range(count):
                node, weight = q.popleft()
                nodes.append(weight)
                
                if node.left : q.append((node.left , 2*weight+1))
                if node.right: q.append((node.right, 2*weight+2))
                    
                
            # compare the resultant width with the width of current level
            width = max(width, max(nodes)-min(nodes)+1)
            
        return width
    
# The concept
# In a complete BT
# Left Child  = 2 * parent index + 1
# Right Child = 2 * parent index + 2
# Width of level = Right Child - Left Child + 1
'''

# Kunal Wadhwa


'''