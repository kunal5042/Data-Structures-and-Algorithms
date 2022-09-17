# Question: https://leetcode.com/problems/binary-search-tree-iterator/
# Medium
from typing import Optional, List

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class BSTIterator:
    # O(1) Time and O(h) Space on average

    def __init__(self, root: Optional[TreeNode]):
        self.callstack = []
        self.fill_callstack(root)

    def next(self) -> int:
        if self.hasNext():
            next_node = self.callstack.pop()
            self.fill_callstack(next_node.right)
            return next_node.val

    def hasNext(self) -> bool:
        return len(self.callstack) != 0
    
    def fill_callstack(self, node):
        while node is not None:
            self.callstack.append(node)
            node = node.left
'''

# Kunal Wadhwa

'''