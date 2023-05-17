# Question: https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/
# Medium


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import List

class Solution(object):
    # O(n) time and O(n) space
    def pairSum(self, head):
        current = head
        values = []

        while current:
            values.append(current.val)
            current = current.next
        
        idx = 0
        jdx = len(values) - 1
        maximum_sum = 0
        
        while(idx < jdx):
            maximum_sum = max(maximum_sum, values[idx] + values[jdx])
            idx += 1
            jdx -= 1
        
        return maximum_sum


# May 17, 2023

'''

# Kunal Wadhwa

'''