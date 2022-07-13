# Question: https://leetcode.com/problems/merge-two-sorted-lists/

from typing import Optional, List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """ Takes two sorted singly linked lists
        Merges the two linked lists and returns the head of the merged list
        """
        if all([not list1, not list2]): return None
        
        dummy = ListNode(-1)
        
        # merge function
        def merge(merged, iter1, iter2):
            while iter1 and iter2:
                if iter1.val < iter2.val:
                    merged.next = iter1
                    iter1 = iter1.next
                else:
                    merged.next = iter2
                    iter2 = iter2.next
                    
                merged = merged.next
                
            merged.next = iter2 if not iter1 else iter1
            
            
        merge(dummy, list1, list2)
        return dummy.next
'''

# Kunal Wadhwa

'''