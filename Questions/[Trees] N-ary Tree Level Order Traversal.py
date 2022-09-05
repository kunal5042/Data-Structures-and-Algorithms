# Question: https://leetcode.com/problems/n-ary-tree-level-order-traversal/
# Medium
from typing import Optional, List

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        def breadth_first_search(node):
            traversal = []
            queue = deque([node])
            
            while len(queue) != 0:
                count = len(queue)
                level = []
                
                for _ in range(count):
                    node = queue.popleft()
                    if node is None:
                        continue
                    level.append(node.val)
                    
                    for child in node.children:
                        queue.append(child)
                        
                    
                traversal.append(level)
                
            return traversal
        
        if not root: return []
        return breadth_first_search(root)
'''

# Kunal Wadhwa

'''