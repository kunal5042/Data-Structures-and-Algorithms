# Question: https://leetcode.com/problems/average-of-levels-in-binary-tree/

from typing import Optional, List
from collections import deque

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        queue = deque()
        queue.append(root)
        result = list()
        while len(queue):
            nodes_count = len(queue)
            nodes_sum_for_current_level = 0
            
            for node_num in range(nodes_count):
                current_node = queue.popleft()
                nodes_sum_for_current_level += current_node.val
                
                if current_node.left is not None:
                    queue.append(current_node.left)
                    
                if current_node.right is not None:
                    queue.append(current_node.right)
                    
                    
            average = nodes_sum_for_current_level / nodes_count
            result.append(average)
            
        return result
    
# Kunal Wadhwa
