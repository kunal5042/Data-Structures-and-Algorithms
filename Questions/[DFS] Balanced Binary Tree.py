# Question: https://leetcode.com/problems/balanced-binary-tree/
# Easy
# 
from typing import Optional, List

class Solution:
    def isBalanced(self, root):
        
        # O(n) Solution
        
        def check_for_balance(root):
            if root is None:
                # if root is None: It's a leaf and it's height from bottom is 0
                # it's a base case and it's considered as balanced
                # so return (is_balanced, current_height)
                return (True, 0)
            
            
            # here left and right will contain the information about left and right subtree
            # as left = (is_balanced_left, heigh_of_left_subtree)
            # so  left[0] = [True|False]
            # and left[1] = [Height (int)]
            
            left  = check_for_balance(root.left)
            right = check_for_balance(root.right)
            
            # current node is considered balanced if it's left and right subtree's height's difference is <= 1
            # and the left and right subtrees are balanced themselves
            is_balanced    = left[0] and right[0] and abs(left[1] - right[1]) <= 1
            
            # current node's height = 1 + maximum of height of left and right subtrees
            current_height = 1 + max(left[1], right[1])
            
            # return information about current node to the parent node
            return (is_balanced, current_height)

        
        return check_for_balance(root)[0]
'''

# Kunal Wadhwa


'''