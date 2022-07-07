# Question: https://leetcode.com/problems/path-sum-ii

from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        result = []
        
        def helper(node, running_sum, target_sum, path):
            if node is None: return
            
            running_sum += node.val
            if running_sum == target_sum and not node.left and not node.right:
                result.append(path + [node.val])
                return
            
            helper(node.left , running_sum, target_sum, path + [node.val])
            helper(node.right, running_sum, target_sum, path + [node.val])
            
            return
        
        def backtrack(node, path, target_sum):
            if node is None: return
            
            path.append(node.val)
            
            if not node.left and not node.right and target_sum - node.val == 0:
                result.append(path.copy())
                path.pop()
                return
            
            backtrack(node.left , path, target_sum-node.val)
            backtrack(node.right, path, target_sum-node.val)
            
            path.pop()
            return
        
        backtrack(root, [], targetSum)
        return result
'''

# Kunal Wadhwa

# GitHub     : https://github.com/kunal5042
# LeetCode   : https://leetcode.com/kunal5042/
# HackerRank : https://www.hackerrank.com/kunalwadhwa_cs
# LinkedIn   : https://www.linkedin.com/in/kunal5042/

'''