# Question: https://leetcode.com/problems/add-two-numbers/
# Medium
from typing import Optional, List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # O(n) Time and O(1) Extra Space
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head1, head2, head3 = l1, l2, ListNode(-1)
        result_reference = head3
        carry = 0
        
        while head1 != None or head2 != None or carry != 0:
            (value1, value2) = (0, 0)
            
            if head1 is not None:
                value1 = head1.val
                
            if head2 is not None:
                value2 = head2.val
                
            result_value = value1 + value2 + carry
            carry = 0
            
            if result_value > 9:
                carry = 1
                result_value -= 10
                
            head3.next = ListNode(result_value)
            head3      = head3.next
            
            head1 = head1.next if head1 is not None else None
            head2 = head2.next if head2 is not None else None
            
        return result_reference.next
            
'''

# Kunal Wadhwa


'''