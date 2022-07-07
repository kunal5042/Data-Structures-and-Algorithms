# Question: https://leetcode.com/problems/path-sum-iii/

from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if root is None: return 0
        result = [0]
        
        def solve(node, prefix_sum, hashmap):
            if node is None: return
            
            prefix_sum += node.val
            if prefix_sum - targetSum in hashmap:
                result[0] += hashmap[prefix_sum-targetSum]
            
            if prefix_sum == targetSum:
                result[0] += 1
            
            hashmap[prefix_sum] = hashmap.get(prefix_sum, 0) + 1
            
            solve(node.left , prefix_sum, hashmap)
            solve(node.right, prefix_sum, hashmap)
            hashmap[prefix_sum] -= 1
            
            return
        
        solve(root, 0, dict())
        return result[0]
'''

# Kunal Wadhwa

# GitHub     : https://github.com/kunal5042
# LeetCode   : https://leetcode.com/kunal5042/
# HackerRank : https://www.hackerrank.com/kunalwadhwa_cs
# LinkedIn   : https://www.linkedin.com/in/kunal5042/

'''