# Question: https://leetcode.com/problems/palindrome-linked-list/
# Easy
from typing import Optional, List

class Solution:
    # O(n) Time and O(1) Space
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # find the middle node using slow and fast method
        slow = head
        fast = head
        
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
            
        # reversing the right half
        current = slow
        previous = None
        while current != None:
            temp         = current.next
            current.next = previous
            previous     = current
            current      = temp
        
        # checking if the linked list is a palindrome
        # this will work for odd and even because
        #   - even: equally divided both halves, can be compared
        #   - odd : both the halves will point to the same node, so it won't be a problem 

        # and that is the reason we reversed the right half and not the left
        
        left = head
        right = previous
        
        while right != None:
            if left.val != right.val:
                return False
            
            left = left.next
            right = right.next
            
        return True
'''

# Kunal Wadhwa


'''