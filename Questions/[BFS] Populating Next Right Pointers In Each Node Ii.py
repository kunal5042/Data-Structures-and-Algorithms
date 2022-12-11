# Question: https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/
# Medium
from typing import Optional, List

# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
        
from collections import deque
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root: return root
        
        q = deque()
        q.append(root)
        
        while len(q):
            count = len(q)
            prev  = None
            for _ in range(count):
                node  = q.popleft()
                
                if node.right: q.append(node.right)
                if node.left : q.append(node.left)
                    
                if prev is not None:
                    node.next  = prev
                    prev       = node
                else:
                    prev       = node
                    
        return root

'''

# Kunal Wadhwa


'''