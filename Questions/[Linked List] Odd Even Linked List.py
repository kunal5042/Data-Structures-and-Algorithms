# Question: https://leetcode.com/problems/odd-even-linked-list/
# Medium
from typing import Optional, List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        

class Solution:
    # O(n) Time and O(n) Space
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or head.next is None: return head
        
        current, tail, length = head, None, 0
        while current:
            tail    = current
            current = current.next
            length += 1
            
        current = head
        prev    = None
        for idx in range(1, length+1):
            # if even node, append it to the end
            # and attach the previous odd node with next odd node
            if idx % 2 == 0:
                prev.next = current.next if current.next is not None else tail
                tail.next = current
                tail = tail.next
                
            # keep track of previous nodes so that we can attach/connect odd
            # nodes later
            prev = current
            current = current.next
            
        # otherwise, we'll have a cycle
        tail.next = None
            
        return head
'''

# Kunal Wadhwa


'''