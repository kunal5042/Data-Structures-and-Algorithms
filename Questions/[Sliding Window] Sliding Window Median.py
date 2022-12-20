# Question: https://leetcode.com/problems/sliding-window-median/
# Hard
# To Do: Solve using two heaps

from typing import Optional, List
import bisect

class LinkedListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution:
    # brute-force: time limit exceeded
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        def median_of_ll(head, k):
            prev = None
            slow = head
            fast = head

            while fast is not None and fast.next is not None:
                prev = slow
                slow = slow.next
                fast = fast.next.next
                
            if k % 2 != 0: return slow.val
            return (prev.val + slow.val) / 2
                
        def insert(node, head):
            previous, current = None, head
            
            while current is not None and node.val > current.val:
                previous = current
                current = current.next
                
            previous.next = node
            node.next = current
            
        def traverse(head):
            current = head
            while current is not None:
                print(current.val, end=' ')
                current = current.next
            print()
            
        def delete(head, node_value):
            previous = None
            current = head
            while current.val != node_value:
                previous = current
                current = current.next
                
            # end
            if current.next is None:
                previous.next = None
                
            else:
                previous.next = current.next
            
        result = []
        dummy = LinkedListNode(float('-inf'))
        
        for idx in range(k):
            insert(LinkedListNode(nums[idx]), dummy)
            
        result.append(median_of_ll(dummy.next, k))
        idx = k
        while idx < len(nums):
            delete(dummy, nums[idx-k])
            insert(LinkedListNode(nums[idx]), dummy)
            result.append(median_of_ll(dummy.next, k))
            idx += 1
            
        return result
    
    # O(n*k) time and O(k) space
    def medianSlidingWindow(self, nums, k):
        window = sorted(nums[:k])
        medians = []
        for a, b in zip(nums, nums[k:] + [0]):
            medians.append((window[k//2] + window[~(k//2)]) / 2.)
            window.remove(a)
            bisect.insort(window, b)
        return medians


# December 20, 2022

'''

# Kunal Wadhwa

'''