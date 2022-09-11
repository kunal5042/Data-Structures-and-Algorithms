# Question: https://leetcode.com/problems/remove-duplicates-from-sorted-list/
# Easy
from typing import Optional, List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # O(n) Time and O(1) Space
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