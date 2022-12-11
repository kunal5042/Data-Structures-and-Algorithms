# Question: https://leetcode.com/problems/intersection-of-two-linked-lists/
# Easy
from typing import Optional, List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # O(max(n, m)) Time and O(max(n, m)) Space
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        visited = set()
        current = headA
        while current is not None:
            visited.add(current)
            current = current.next
            
        current = headB
        while current is not None:
            if current in visited:
                return current
            current = current.next
            
        return
    
    # O(n + m) Time and O(1) Space
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        dum_a, dum_b = headA, headB
        
        while dum_a != dum_b:
            dum_a = headB if dum_a is None else dum_a.next
            dum_b = headA if dum_b is None else dum_b.next
            
        return dum_a
'''

# Kunal Wadhwa

'''