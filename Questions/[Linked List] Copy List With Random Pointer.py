# Question: https://leetcode.com/problems/copy-list-with-random-pointer/
# Medium
from typing import Optional, List

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    # O(n) Time and O(n) Space
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        copies = {}
        
        current = head
        # copy of each node
        while current is not None:
            copies[current] = Node(current.val)
            current = current.next
            
        current = head
        # linking copies
        while current is not None:
            if current.next is not None:
                copies[current].next = copies[current.next]
                
            if current.random is not None:
                copies[current].random = copies[current.random]
            
            current = current.next
        
        for head in copies: return copies[head]

'''

# Kunal Wadhwa

'''