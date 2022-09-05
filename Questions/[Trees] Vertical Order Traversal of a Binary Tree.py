# Question: https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/
# Hard
#
from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
from collections import defaultdict
from heapq import heappush as heap_push, heappop as heap_pop
class Solution:
    # O(n * log(n)) Time and O(n) Space
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        groups = defaultdict(list)
        
        def preorder(node, column, depth):
            if node is None:
                return
            
            heap_push(groups[column], (depth, node.val))
            
            preorder(node.left , column-1, depth+1)
            preorder(node.right, column+1, depth+1)
            
            
        preorder(root, 0, 0)
        
        unordered_result = []
        for column, group in groups.items():
            unordered_result.append([column, [heap_pop(group)[1] for _ in range(len(group))]])
            
        return list(map(lambda x: x[1], sorted(unordered_result, key = lambda x: x[0])))

'''

# Kunal Wadhwa

'''