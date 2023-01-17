# Question: https://leetcode.com/problems/house-robber-iii/
# Medium
from typing import Optional, List

from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    # WA: we are linking all nodes at given level
    # thereby eliminating the possiblity of skipping 
    # some nodes at given level in order to maximize money
    def rob(self, root: Optional[TreeNode]) -> int:
        levels = []
        
        queue = deque([root])
        
        while len(queue) != 0:
            nodes = len(queue)
            this_level = 0
            
            for _ in range(nodes):
                node = queue.popleft()
                if node.left is not None: queue.append(node.left)
                if node.right is not None: queue.append(node.right) 
                this_level += node.val
                
            levels.append(this_level)
            
        if len(levels) <= 2: return max(levels)
        can_rob, prev_robbed = 0, levels[0]
        
        print(levels)
        for idx in range(1, len(levels)):
            temp = prev_robbed
            prev_robbed = max(prev_robbed, can_rob+levels[idx])
            can_rob = temp
            
        return max(can_rob, prev_robbed)
    
    # O(n) time and O(h) space
    def rob(self, root: Optional[TreeNode]) -> int:
        def optimal_rob(node):
            if node is None:
                return (0, 0)
            
            left = optimal_rob(node.left)
            right = optimal_rob(node.right)
            
            robbed = node.val + left[1] + right[1]
            skipped = max(left) + max(right)
            
            return (robbed, skipped)
        
        return max(optimal_rob(root))


# January 17, 2023

'''

# Kunal Wadhwa

'''