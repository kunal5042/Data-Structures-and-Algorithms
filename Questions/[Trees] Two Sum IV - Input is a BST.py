# Question: https://leetcode.com/problems/two-sum-iv-input-is-a-bst/
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
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        stack = []
        cache = set()
        
        while root is not None or len(stack) != 0:
            while root is not None:
                stack.append(root)
                root = root.left
                
            root = stack.pop()
            if k - root.val in cache:
                return True
            
            cache.add(root.val)

            root = root.right
                
        return False
'''

# Kunal Wadhwa

'''