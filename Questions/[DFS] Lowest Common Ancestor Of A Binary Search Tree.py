# Question: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
# Easy
# To Do: Read the question carefully. Given tree is a BST
from typing import Optional, List

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class NodeInfo:
    def __init__(self, parent, depth):
        self.parent = parent
        self.depth  = depth

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def get_node_information(node, parent=None, depth=0, hashmap=dict()):
            if node is None:
                return
            
            hashmap[node] = NodeInfo(parent, depth)
            
            get_node_information(node.left , node, depth+1, hashmap)
            get_node_information(node.right, node, depth+1, hashmap)            
            
            return hashmap
        
        tree_nodes_info = get_node_information(root)
        
        difference_in_depths = abs(tree_nodes_info[p].depth - tree_nodes_info[q].depth)
        deeper_node          = max(p, q, key=lambda x: tree_nodes_info[x].depth)
        node                 = min(q, p, key=lambda x: tree_nodes_info[x].depth)
        
        print(deeper_node.val)
        print(node.val)
        print(difference_in_depths)

        
        for _ in range(difference_in_depths):
            deeper_node = tree_nodes_info[deeper_node].parent
            
        if deeper_node == node: return node
        
        while tree_nodes_info[node].parent:
            deeper_node = tree_nodes_info[deeper_node].parent
            node        = tree_nodes_info[node].parent
            
            if node == deeper_node:
                return node
            
        return None

# Kunal Wadhwa
