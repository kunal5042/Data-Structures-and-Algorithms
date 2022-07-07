# Question: https://leetcode.com/problems/binary-tree-right-side-view/

from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return list()
        
        q = deque([root])
        right_view = list()
        
        while len(q):
            count = len(q)
            for _ in range(count):
                node = q.popleft()
                
                count -= 1
                if count == 0:
                    right_view.append(node.val)
                    
                if node.left : q.append(node.left)
                if node.right: q.append(node.right)
                    
                    
        return right_view
                    
                
'''

# Kunal Wadhwa

# GitHub     : https://github.com/kunal5042
# LeetCode   : https://leetcode.com/kunal5042/
# HackerRank : https://www.hackerrank.com/kunalwadhwa_cs
# LinkedIn   : https://www.linkedin.com/in/kunal5042/

'''