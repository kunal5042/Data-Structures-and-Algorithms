# Question: https://leetcode.com/problems/delete-node-in-a-linked-list/
# Medium

class Solution:
    # O(n) Time and O(1) Space
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        current  = node
        previous = None
        while current is not None and current.next is not None:
            current.val = current.next.val
            previous    = current
            current     = current.next
            
        previous.next = None
        
# Kunal Wadhwa