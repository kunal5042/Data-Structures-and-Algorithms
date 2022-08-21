# Question: https://leetcode.com/problems/linked-list-in-binary-tree/
# Medium
# To Do: Solve using KMP Algorithm
from typing import Optional, List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    # O(n+m) Time
    # where n is the length of the linked list
    # and m is the number of nodes in the tree
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        result = [False]
        DELIMITER = ';'
        
        link_list = []
        current = head
        while current is not None:
            link_list.append(str(current.val))
            current = current.next
            
        # so, that numbers don't get mixed up
        link_list = DELIMITER.join(link_list)
        
        def find(tree_node, path):
            # finds if link_list string is a substring of this path
            if link_list in path:
                return True
            
            if tree_node is None:
                return False
            
            path += str(tree_node.val) + DELIMITER
            
            return find(tree_node.left, path) or find(tree_node.right, path)
        
        return find(root, '')
'''

# Kunal Wadhwa

'''