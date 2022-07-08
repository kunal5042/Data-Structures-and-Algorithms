# Question: https://leetcode.com/problems/maximum-binary-tree/

from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums) == 0: return TreeNode()
        
        def construct(parent, direction, start, end, nums):
            if start > end: return
            
            child      = child_index(start, end, nums)
            new_parent = attach(nums[child], parent, direction)
            construct(new_parent, 'left' , start  , child-1, nums)
            construct(new_parent, 'right', child+1, end, nums)
            return parent
            
            
        def attach(node_val, parent, direction):
            node = TreeNode(node_val)
            if direction == 'left':
                parent.left = node 
            else:
                parent.right = node
            return node

        def child_index(start, end, nums):
            idx    = start
            result = None
            cmax   = float('-inf')
            while idx <= end:
                if nums[idx] > cmax:
                    cmax = nums[idx]
                    result = idx
                idx += 1
                
            return result
                
        root = float('-inf')
        root_idx = None
        for idx in range(len(nums)):
            if nums[idx] > root:
                root = nums[idx]
                root_idx = idx
                
        root = TreeNode(nums[root_idx])
        construct(root, 'left', 0, root_idx-1, nums)
        construct(root, 'right', root_idx +1, len(nums)-1, nums)
        return root
'''

# Kunal Wadhwa


'''