# Question: https://leetcode.com/problems/same-tree/
# Easy
# Traverse together
from typing import List, Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # DFS Solution
        def helper(p, q):
            if p is None and q is not None  : return False
            if q is None and p is not None  : return False
            if p is None and q is None      : return True
            if p.val != q.val               : return False
            
            return True and helper(p.left, q.left) and helper(p.right, q.right)
        
        return helper(p,q)

        
    def BFS_solution(self, p, q):
        if p == None and q == None: return True
        if q == None: return False
        if p == None: return False
        
        
        # BFS Solution
        q1, q2 = deque(), deque()
        
        q1.append(p)
        q2.append(q)
        
        result = True
        
        while len(q1) and len(q2):
            c1, c2 = q1.popleft(), q2.popleft()
            
            if c1.val != c2.val:
                return False
            
            if (c1.left is None and c2.left is not None) or (c1.left is not None and c2.left is None):
                return False
            
            if (c1.right is None and c2.right is not None) or (c1.right is not None and c2.right is None):
                return False
                
            if c1.left is not None:
                q1.append(c1.left)
                q2.append(c2.left)

            if c2.right is not None:
                q1.append(c1.right)
                q2.append(c2.right)
                
        return True
                    
# Kunal Wadhwa
