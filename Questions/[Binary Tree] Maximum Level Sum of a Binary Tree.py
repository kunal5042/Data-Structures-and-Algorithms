# Question: https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/description/
# Medium

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque
from typing import Optional

class Solution:
    # O(n) time and O(max_width) space
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if root is None: return 1
        max_sum = root.val
        level = 0
        max_level = 1
        queue = deque([root])

        while len(queue) != 0:
            count = len(queue)
            level_sum = 0
            level += 1

            for _ in range(count):
                node = queue.popleft()
                level_sum += node.val

                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)

            if max_sum < level_sum:
                max_sum = level_sum
                max_level = level

        return max_level


# June 15, 2023

'''

# Kunal Wadhwa

'''