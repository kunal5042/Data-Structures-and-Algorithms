# Question: https://leetcode.com/problems/swap-nodes-in-pairs/
# Medium
from typing import Optional, List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from collections import deque
class Solution:
    # O(n) Time and O(n) Space
    def _swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None: return head
        
        result = head.next
        
        q = []
        first, second = head, head.next
        q.append((first, second))
        
        while first and second and second.next:
            first = first.next.next
            second = second.next.next
            q.append((first, second))
            
            
        def reverse(first, second):
            if not second:
                return first, None
            second.next = first
            first.next  = None
            return second, first
        
        for idx in range(len(q)):
            first, second = q[idx]
            q[idx] = reverse(first, second)
            if idx != 0:
                q[idx-1][1].next = q[idx][0]

        return result
    
    
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(None, head)
        prev, cur = dummy, head
        while cur and cur.next:
            prev.next = cur.next
            cur.next = cur.next.next
            prev.next.next = cur
            prev, cur = cur, cur.next
        return dummy.next
'''

# Kunal Wadhwa


'''