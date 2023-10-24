# Question: https://leetcode.com/problems/find-largest-value-in-each-tree-row/
# Medium

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque
from typing import Optional, List

class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        """
        @param root: Root of the binary tree of type TreeNode
        @return List[int]: List of the largest values at each level of the binary tree
        time - O(n) space - O(n)
        """
        queue = deque([root])
        result = []
        
        if root is None: return result
        
        while len(queue) != 0:
            level_width = len(queue)
            level_largest = float('-inf')
            
            for _ in range(level_width):
                node = queue.popleft()
                level_largest = max(level_largest, node.val)
                if node.left is not  None: queue.append(node.left)
                if node.right is not None: queue.append(node.right)
                    
            result.append(level_largest)
            
        return result
        
        


# October 24, 2023

'''

# Kunal Wadhwa

'''