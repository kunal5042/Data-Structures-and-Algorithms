# Question: https://leetcode.com/problems/all-elements-in-two-binary-search-trees/
# Medium
from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        def inorder(node, traversal):
            if node is None:
                return traversal
            
            inorder(node.left, traversal)
            traversal.append(node.val)
            inorder(node.right, traversal)
            
            return traversal
        
        tree1 = inorder(root1, [])
        tree2 = inorder(root2, [])
        
        iter1, iter2 = 0, 0
        result = []
        
        while iter1 < len(tree1) and iter2 < len(tree2):
            if tree1[iter1] < tree2[iter2]:
                result.append(tree1[iter1])
                iter1 += 1
            else:
                result.append(tree2[iter2])
                iter2 += 1
                
        while iter1 < len(tree1):
            result.append(tree1[iter1])
            iter1 += 1
            
        while iter2 < len(tree2):
            result.append(tree2[iter2])
            iter2 += 1
            
        return result
'''

# Kunal Wadhwa

'''