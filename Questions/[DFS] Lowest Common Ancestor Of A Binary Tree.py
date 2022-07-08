# Question: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/

from typing import Optional, List

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Given
        # All node values are unique
        # p and q will exist in the tree
        # p != q
        
        # this function will store the immediate parent of every node
        # in the parents dictionary as a key, value pair
        # where key = current node and value = immediate parent
        def get_parents(root, parent, parents):
            if root is None:
                return
            
            parents[root] = parent
            get_parents(root.left, root, parents)
            get_parents(root.right, root, parents)
            return
        
        
        # this function will find the target node in the tree
        # given that the target node exist in the tree
        # and return it's depth in the tree
        def get_depth(root, target, depth=0):
            if root == None:
                return -1
            
            if root == target:
                return depth
            
            left = get_depth(root.left, target, depth+1)
            right = get_depth(root.right, target, depth+1)
            
            return left if left != -1 else right
        
        # this is our parents dictionary
        parents = {}
        # getting parents of all the nodes
        get_parents(root, None, parents)
        
        # finding the depths of both the given nodes
        depth_p = get_depth(root, p)
        depth_q = get_depth(root, q)
        
        
        # we will bring both the nodes to the same level
        # so that, we will find which node has more depth
        # and bring it up to the same level as the other node
        
        if depth_p > depth_q:
            # bring p to the same level
            move_up = depth_p - depth_q
            
            for _ in range(move_up):
                p = parents[p]
                

            
        if depth_q > depth_p:
            # bring q to the same level
            move_up = depth_q - depth_p
            
            for _ in range(move_up):
                q = parents[q]
                
        
        # once both nodes are on the same level, we will check
        # if they are the same
        # case: where p is ancestor of q or q is ancestor of p
        if p == q:
            return p
        
        # now, both the nodes are at the same level
        # traverse up till we find a common ancestor
        while p is not None or q is not None:
            if p == q:
                return p
            p = parents[p]
            q = parents[q]
            
        return 'No common parent was found'
    
'''

# Kunal Wadhwa


'''