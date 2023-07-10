# Question: https://leetcode.com/problems/minimum-depth-of-binary-tree/
# Easy

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque
from typing import Optional

class Solution:
    # O(2^height) space and O(n) time
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        queue = deque()
        queue.append(root)
        level = 1

        while len(queue) != 0:
            count_of_nodes = len(queue)
            for _ in range(count_of_nodes):
                node = queue.popleft()
                # leaf node
                if node.left is None and node.right is None:
                    return level
                
                if node.left is not None:
                    queue.append(node.left)

                if node.right is not None:
                    queue.append(node.right)

            level += 1

        return Exception("We are not supposed to reach here")


# July 10, 2023

'''

# Kunal Wadhwa

'''