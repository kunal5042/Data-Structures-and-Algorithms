# Question: https://leetcode.com/problems/maximum-depth-of-binary-tree/

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None: return 0
        
        # DFS Solution
        def helper(node, depth=0):
            if node is None:
                return depth
            
            return max(depth, helper(node.left, depth+1), helper(node.right, depth+1))
        
        
        return helper(root)
# Kunal Wadhwa
