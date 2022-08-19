# Question: https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/

# Easy
from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # O(n * log(n)) Time and O(n/2) Recursion call-stack space
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        def insert(child_value, parent):
            if child_value < parent.val:
                parent.left = TreeNode(child_value)
                return parent.left
            else:
                parent.right = TreeNode(child_value)
                return parent.right
            
        
        def partition(start, end, parent):
            if start >= 0 and end < len(nums) and start <= end:
                middle = (start + end) // 2
                new_parent = insert(nums[middle], parent)
                partition(start   , middle-1, new_parent)
                partition(middle+1, end     , new_parent)
                
        
        root = TreeNode(nums[len(nums)//2])
        partition(0, len(nums)//2-1, root)
        partition(len(nums)//2+1, len(nums)-1, root)
        
        return root
'''

# Kunal Wadhwa

'''