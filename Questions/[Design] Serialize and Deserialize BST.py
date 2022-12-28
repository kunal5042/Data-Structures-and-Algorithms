# Question: https://leetcode.com/problems/serialize-and-deserialize-bst/
# Medium
from typing import Optional, List

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """
        data = ''
        def preorder(node):
            if node is None: return
            nonlocal data
            data +=  ' ' + str(node.val)
            preorder(node.left)
            preorder(node.right)
            
        preorder(root)
        return data.strip()

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """
        if len(data) == 0: return None
        preorder = [int(num) for num in data.split(' ')]
        inorder = sorted(preorder)
        indices = {val:idx for idx, val in enumerate(inorder)}
        root_idx = 0
        
        def rooting(left, right):
            nonlocal root_idx

            if left > right:
                return None
            
            root = TreeNode(preorder[root_idx])
            root_idx += 1
            
            root.left  = rooting(left, indices[root.val] - 1)
            root.right = rooting(indices[root.val] + 1, right)
            
            return root
        
        return rooting(0, len(preorder)-1)
        
        

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans


# December 28, 2022

'''

# Kunal Wadhwa

'''