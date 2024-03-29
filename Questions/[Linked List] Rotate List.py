# Question: https://leetcode.com/problems/rotate-list/
# Medium
from typing import Optional, List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # O(n) Time and O(1) Extra Space
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 0: return head
        
        current, length = head, 0
        while current is not None:
            current = current.next
            length += 1
            
        nodes_from_behind = k if k < length else k % length
        if nodes_from_behind == 0 or length == 1: return head

        slow, fast = head, head
        
        count = nodes_from_behind
        while count > 0:
            fast = fast.next
            count -= 1
            
        while fast.next is not None:
            slow = slow.next
            fast = fast.next
            
        new_head = slow.next
        slow.next = None
        
        current = new_head
        while current.next is not None:
            current = current.next
            
        current.next = head
        
        return new_head
        
        
'''

# Kunal Wadhwa


'''