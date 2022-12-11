# Question: https://leetcode.com/problems/remove-nth-node-from-end-of-list/
# Medium
from typing import Optional, List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # O(n) Time and O(1) Space  
    def removeNthFromEnd(self, head: Optional[ListNode], n: int):
        if head is None : return head
        if head.next is None:
            head = None
            return head
        
        fast = head
        while n > 0 :
            fast = fast.next
            n -= 1
            
        if fast is None:
            head = head.next
            return head
        
        slow = head
        while fast and fast.next:
            fast  = fast.next
            slow = slow.next
        
        slow.next = slow.next.next
        return head
    
    # O(n) Time and O(1) Space  
    def removeNthFromEndLength(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow   = head
        length = 0
        
        while slow:
            slow    = slow.next
            length += 1
            
        move_forward = length - n
        
        previous, current = None, head
        for _ in range(move_forward):
            previous = current
            current  = current.next
            
        if not previous: return head.next
        
        previous.next = current.next
        return head
        
    
    # O(n) Time and O(n) Space  
    def removeNthFromEndArray(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head: return
        current   = head
        traversal = []
        while current is not None:
            traversal.append(current)
            current = current.next
        
        
        if (n == 1 or n == len(traversal)) and len(traversal) < 2: return
        
        if n == len(traversal): return traversal[1]
        if n == 1:
            traversal[~1].next = None
            return traversal[0]
        
        traversal[-n-1].next = traversal[-n].next
        return head

'''

# Kunal Wadhwa


'''