# Question: https://leetcode.com/problems/reorder-list/

from typing import Optional, List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        def reverse(node):
            previous = None
            current  = node
            while node is not None:
                temp = node.next
                node.next = previous
                previous = node
                node = temp
            
            return previous
        
        def insert_after(node, to_insert):
            temp = node.next
            node.next = to_insert
            to_insert.next = temp
            return node
        
        slow, fast, prev = head, head, None
        while slow and fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
            
        # reverse second half
        head2 = reverse(slow.next)
        # disconnect
        slow.next = None
        
        pointer1, pointer2 = head, head2
        
        while pointer2:
            temp = pointer2.next
            insert_after(pointer1, pointer2)
            pointer1 = pointer1.next.next
            pointer2 = temp
            
        return head
'''

# Kunal Wadhwa


'''