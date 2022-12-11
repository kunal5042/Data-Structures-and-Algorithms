# Question: https://leetcode.com/problems/minimum-depth-of-binary-tree/
# Easy
from collections import deque
class Solution:
    # O(V) time 
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None: return 0
        
        result = float('inf')
        queue  = deque()
        queue.append(root)
        depth = 0
        while len(queue):
            depth     += 1
            node_count = len(queue)
            
            for node_number in range(node_count):
                node = queue.popleft()
                # shortest path from root node down to nearest leaf
                if node.left is None and node.right is None:
                    result = min(result, depth)
                    
                if node.left is not None : queue.append(node.left)
                if node.right is not None: queue.append(node.right)
                    
                    
        return result
# Kunal Wadhwa
