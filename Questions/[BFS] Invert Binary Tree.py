# Question: https://leetcode.com/problems/invert-binary-tree/

from collections import deque
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None: return root
        
        # BFS Solution
        queue = deque()
        queue.append(root)
        
        while len(queue):
            nodes_count = len(queue)
            
            for node_number in range(nodes_count):
                node = queue.popleft()
                node.left, node.right = node.right, node.left
                
                if node.left is not None: queue.append(node.left)
                if node.right is not None: queue.append(node.right)
                    
        return root
    
    # DFS Solution
    def reverse(self, root):
        if root is None:
            return
        
        root.left, root.right = root.right, root.left
        
        # this node has been reversed
        # now we reverse it's children recursively 
        
        self.reverse(root.left)
        self.reverse(root.right)
        
        return root

# Kunal Wadhwa
