# Question: https://leetcode.com/problems/remove-zero-sum-consecutive-nodes-from-linked-list/
# Medium
from typing import Optional, List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # O(n) time and O(n) space
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        current = head
        prefix = {0: dummy}
        psum = 0
        
        while current is not None:
            psum += current.val
            
            # if consecutive summed upto zero
            if psum in prefix:
                # nodes to skip
                start = prefix[psum]
                start.next = current.next
                
                # reinit psum
                psum = 0
                current = dummy
                
                # reinit hashmap
                prefix = {}
            
            else:
                prefix[psum] = current
                current = current.next
                
        return dummy.next


# January 16, 2023

'''

# Kunal Wadhwa

'''