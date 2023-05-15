# Question: https://leetcode.com/problems/swapping-nodes-in-a-linked-list/
# Medium

from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Initialize two pointers, first and last to the head node.
        first = last = head

        # Traverse the list till kth node using first pointer.
        for _ in range(1, k):
            first = first.next

        # Check if first pointer is at the end of the list
        # If not, move both first and last pointers by one node until we reach the end of the list.
        # At the end of this loop, the last pointer should be pointing to the (kth node from end).
        # At the same time, the first pointer should be pointing to the kth node from the start.
        # This is possible because the difference between first and last pointers is always k.
        last_kth = first
        while last_kth.next:
            last_kth = last_kth.next
            last = last.next

        # Swap the values of kth node from start and kth node from end.
        first.val, last.val = last.val, first.val

        # Return the head node of the modified linked list.
        return head
    



# May 15, 2023

'''

# Kunal Wadhwa

'''