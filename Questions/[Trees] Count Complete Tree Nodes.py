# Question: https://leetcode.com/problems/count-complete-tree-nodes/
# Medium
from typing import Optional, List

# O(log(n) * log(n)) time and O(h) space
class Solution:
    def countNodes(self, root) -> int:
        def get_height(node, direction):
            if node is None: return 1
            height = 2
            while direction == 'L' and node.left is not None:
                node = node.left
                height += 1
            while direction == 'R' and node.right is not None:
                node = node.right
                height += 1
            return height
        
        def count_nodes(node):
            if node is None: return 0
            left  = get_height(node.left, 'L')
            right = get_height(node.right, 'R')
            
            if left == right: return 2**(left) - 1
            return 1 + count_nodes(node.left) + count_nodes(node.right)
        
        return count_nodes(root)
'''

# Kunal Wadhwa

'''