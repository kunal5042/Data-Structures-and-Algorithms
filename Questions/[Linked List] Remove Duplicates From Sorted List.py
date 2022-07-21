# Question: https://leetcode.com/problems/remove-duplicates-from-sorted-list/

from typing import Optional, List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = previous = ListNode(101)
        current  = head
        while current is not None:
            if current.val != previous.val:
                previous.next = current
                previous = current
            current = current.next
            
        previous.next = None
        return dummy.next
'''

# Kunal Wadhwa

'''