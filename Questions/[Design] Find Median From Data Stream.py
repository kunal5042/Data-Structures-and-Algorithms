# Question: https://leetcode.com/problems/find-median-from-data-stream/
# Hard
# Two Heaps
from typing import Optional, List

import heapq
class MedianFinder:

    def __init__(self):
        self.median_handler = ContinuousMedianHandler()

    def addNum(self, num: int) -> None:
        self.median_handler.insert(num)

    def findMedian(self) -> float:
        return self.median_handler.getMedian()

class ContinuousMedianHandler:
    def __init__(self):
        self.median = None
        self.lower_half = MaxHeap()
        self.upper_half = MinHeap()

    def insert(self, number):
        if len(self.lower_half) == 0 or number < self.lower_half.peek():
            self.lower_half.insert(number) 
        else:
            self.upper_half.insert(number)

        self.rebalance_heaps()

    def rebalance_heaps(self):
        if abs(len(self.lower_half) - len(self.upper_half)) > 1:
            if len(self.lower_half) > len(self.upper_half):
                self.upper_half.insert(self.lower_half.remove())
            else:
                self.lower_half.insert(self.upper_half.remove())

        self.update_median()

    def update_median(self):
        if len(self.lower_half) == len(self.upper_half):
            self.median = (self.upper_half.peek() + self.lower_half.peek()) / 2
        else:
            if len(self.lower_half) > len(self.upper_half):
                self.median = self.lower_half.peek()
            else:
                self.median = self.upper_half.peek()

    def getMedian(self):
        return self.median
    
'''
Max Heap Implementation
'''
class MaxHeap:
    def __init__(self):
        self.heap = []

    def sift_up(self):
        child_idx = len(self.heap)-1
        parent_idx = (len(self.heap)-1)//2
        while parent_idx >= 0:
            if self.heap[parent_idx] < self.heap[child_idx]:
                self.swap(parent_idx, child_idx)
                child_idx = parent_idx
                parent_idx = (child_idx-1)//2
            else:
                break

    def sift_down(self, node_idx):
        endidx = len(self.heap)-1
        child_one = (2 * node_idx ) + 1
        while child_one <= endidx:
            child_two = (2 * node_idx) + 2 if (2 * node_idx) + 2 < endidx else None
            
            if child_two is not None:
                if self.heap[child_one] > self.heap[child_two]:
                    to_compare_with = child_one
                else:
                    to_compare_with = child_two
            else:
                to_compare_with = child_one
                
            if self.heap[node_idx] < self.heap[to_compare_with]:
                self.swap(node_idx, to_compare_with)
                
                node_idx = to_compare_with
                child_one = (2 * node_idx) + 1
            
            else:
                break

    def peek(self):
        return self.heap[0]

    def remove(self):
        self.swap(0, len(self.heap)-1)
        maximum_ele = self.heap.pop()
        self.sift_down(0)
        return maximum_ele

    def insert(self, value):
        self.heap.append(value)
        self.sift_up()

    def swap(self, x, y):
        self.heap[x], self.heap[y] = self.heap[y], self.heap[x]

    def __str__(self):
        return str(self.heap)
        
    def __len__(self):
        return len(self.heap)

'''
Min Heap Implementation Using heapq module
'''
class MinHeap:
    def __init__(self):
        self.heap = []
        heapq.heapify(self.heap)
        
    def insert(self, value):
        heapq.heappush(self.heap, value)
        
    def remove(self):
        return heapq.heappop(self.heap)
    
    def peek(self):
        return self.heap[0] if len(self.heap) > 0 else 'Empty'

    def __str__(self):
        return str(self.heap)

    def __len__(self):
        return len(self.heap)

'''

# Kunal Wadhwa

'''