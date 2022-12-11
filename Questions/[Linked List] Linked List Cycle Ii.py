# Question: https://leetcode.com/problems/linked-list-cycle-ii/
# Medium
from typing import Optional, List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return
        
        slow, fast = head, head
        cycle = False
        
        while slow is not None and fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                cycle = True
                break
            
        if not cycle: return
        
        slow = head
        
        while slow != fast:
            slow = slow.next
            fast = fast.next
            
        return slow
'''

# Kunal Wadhwa


'''