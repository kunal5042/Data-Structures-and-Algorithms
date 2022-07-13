# Question: https://leetcode.com/problems/remove-linked-list-elements/

from typing import Optional, List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        """Given head of a linked list and a value, remove all nodes with val == value
        Returns the new head of the linked list
        """
        if not head: return
        
        prev, current = ListNode(-1), head
        prev.next = head
        result = prev
        
        while current is not None:
            if current.val == val:
                prev.next = current.next
            else:
                prev = current
                
            current = current.next
            
            
        return result.next
'''

# Kunal Wadhwa

'''