# Question: https://leetcode.com/problems/partition-list/

from typing import Optional, List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:

        smaller, larger = ListNode(5042), ListNode(5010)
        
        smaller_head, larger_head = smaller, larger
        
        current = head
        while current is not None:
            if current.val < x:
                smaller.next = current
                smaller = smaller.next
            else:
                larger.next = current
                larger = larger.next
                
            current = current.next
            
            
        smaller.next = larger_head.next
        larger.next  = None
        
        return smaller_head.next
'''

# Kunal Wadhwa

'''