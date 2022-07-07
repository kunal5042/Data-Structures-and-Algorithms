# Question: https://leetcode.com/problems/sort-list/

from typing import Optional, List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        def traverse(head):
            current = head
            while current is not None:
                print(current.val, end=' ')
                current = current.next
        
        def merge_sorted_lists(list1, list2):
            pointer1 = list1
            pointer2 = list2
            
            sorted_head = None
            return_head = None
            
            while pointer1 != None or pointer2 != None:
                if sorted_head is None:
                    if pointer1 != None and pointer2 != None:
                        if pointer1.val < pointer2.val:
                            sorted_head = pointer1
                            pointer1    = pointer1.next
                        
                        else:
                            sorted_head = pointer2
                            pointer2    = pointer2.next
                    else:
                        if pointer1 is not None:
                            sorted_head = pointer1
                            pointer1    = pointer1.next

                        if pointer2 is not None:
                            sorted_head = pointer2
                            pointer2    = pointer2.next
                            
                    # store this reference for later
                    return_head = sorted_head
                else:
                    if pointer1 != None and pointer2 != None:
                        if pointer1.val < pointer2.val:
                            sorted_head.next = pointer1
                            pointer1    = pointer1.next
                            sorted_head = sorted_head.next
                        
                        else:
                            sorted_head.next = pointer2
                            pointer2    = pointer2.next
                            sorted_head = sorted_head.next
                        
                    else:
                        if pointer1 is not None:
                            sorted_head.next = pointer1
                            pointer1 = pointer1.next
                            sorted_head = sorted_head.next
                        
                        if pointer2 is not None:
                            sorted_head.next = pointer2
                            pointer2 = pointer2.next
                            sorted_head = sorted_head.next
                            
            sorted_head.next = None
            return return_head
        
        # merge sort
        def merge_sort(head):
            # base case
            if head is None or head.next is None:
                return head
            
            # divide into two parts
            slow = head
            fast = head
            
            while fast.next != None and fast.next.next != None:
                slow = slow.next
                fast = fast.next.next
                
            # slow holds the end of the first half
            head_second_half = slow.next
            
            # separate the first half
            slow.next = None
            
            head_first_half = head
            
            return merge_sorted_lists(merge_sort(head_second_half), merge_sort(head_first_half))
        
        return merge_sort(head)
'''

# Kunal Wadhwa

# GitHub     : https://github.com/kunal5042
# LeetCode   : https://leetcode.com/kunal5042/
# HackerRank : https://www.hackerrank.com/kunalwadhwa_cs
# LinkedIn   : https://www.linkedin.com/in/kunal5042/

'''