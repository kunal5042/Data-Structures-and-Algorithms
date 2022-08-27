# Question: https://leetcode.com/problems/merge-k-sorted-lists/
# Hard
from typing import Optional, List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # O(k * n) where k is number of linked lists and O(n) Space
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        def merge(head1, head2):
            if head1 is None: return head2
            if head2 is None: return head1
            
            sorted_list = ListNode(-1)
            return_head = sorted_list

            iter1, iter2 = head1, head2
            
            while iter1 is not None and iter2 is not None:
                if iter1.val <= iter2.val:
                    sorted_list.next = ListNode(iter1.val)
                    sorted_list = sorted_list.next
                    iter1 = iter1.next
                else:
                    sorted_list.next = ListNode(iter2.val)
                    sorted_list = sorted_list.next
                    iter2 = iter2.next
                    
            while iter1 is not None:
                sorted_list.next = ListNode(iter1.val)
                sorted_list = sorted_list.next
                iter1 = iter1.next
                
            while iter2 is not None:
                sorted_list.next = ListNode(iter2.val)
                sorted_list = sorted_list.next
                iter2 = iter2.next
                
            return return_head.next
        
        sorted_list = None
        for linked_list in lists:
            sorted_list = merge(sorted_list, linked_list)
            
        return sorted_list
    
    # O(n * log(n)) Time and O(n) Space
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        lists_combined = []
        for linked_list in lists:
            while linked_list is not None:
                lists_combined.append(linked_list.val)
                linked_list = linked_list.next
                
        lists_combined.sort()
        sorted_list = ListNode(-1)
        head = sorted_list
        
        for ele in lists_combined:
            head.next = ListNode(ele)
            head = head.next
            
        return sorted_list.next
    
    # O(n * log(n)) Time and O(n) Space
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def merge(head1, head2):
            if head1 is None: return head2
            if head2 is None: return head1
            
            sorted_list = ListNode(-1)
            return_head = sorted_list

            iter1, iter2 = head1, head2
            
            while iter1 is not None and iter2 is not None:
                if iter1.val <= iter2.val:
                    sorted_list.next = ListNode(iter1.val)
                    sorted_list = sorted_list.next
                    iter1 = iter1.next
                else:
                    sorted_list.next = ListNode(iter2.val)
                    sorted_list = sorted_list.next
                    iter2 = iter2.next
                    
            while iter1 is not None:
                sorted_list.next = ListNode(iter1.val)
                sorted_list = sorted_list.next
                iter1 = iter1.next
                
            while iter2 is not None:
                sorted_list.next = ListNode(iter2.val)
                sorted_list = sorted_list.next
                iter2 = iter2.next
                
            return return_head.next
        
        def merge_sort(start, end):
            if start == end: return lists[start]
            if start  > end: return None
            middle = (start + end) // 2
            left_half   = merge_sort(start, middle)
            right_half  = merge_sort(middle+1, end)
            sorted_list = merge(left_half, right_half)
            return sorted_list
        
        return merge_sort(0, len(lists)-1)
'''

# Kunal Wadhwa

'''