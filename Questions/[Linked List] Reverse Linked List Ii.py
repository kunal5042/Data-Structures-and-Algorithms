# Question: https://leetcode.com/problems/reverse-linked-list-ii/
# Medium
from typing import Optional, List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # O(n) Time and O(1) Space
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if head is None or left == right: return head
        
        def reverse(node, nodecount):
            head = node
            prev = None
            for _ in range(nodecount):
                temp = node.next
                node.next = prev
                prev = node
                node = temp
            
            if node is not None:
                head.next = node
                
            return prev
            
        prevleft, current = None, head
        count = 1
        while current is not None and count != left:
            prevleft = current
            current = current.next
            count  += 1
            if count == left:
                break
                
        if not current : return prevleft
        if not prevleft:
            return reverse(head, right-left+1)
                
        prevleft.next = reverse(current, right-left+1)
        return head
        
'''

# Kunal Wadhwa


'''