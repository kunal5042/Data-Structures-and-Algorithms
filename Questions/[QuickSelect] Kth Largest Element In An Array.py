# Question: https://leetcode.com/problems/kth-largest-element-in-an-array/

from typing import Optional, List

# Max Heap Implementation
class MaxHeap:
    def __init__(self, array=list()):
        self.heap = array
        self.heapify(array)
        
    # Builds Heap in O(n) Time
    def heapify(self, array):
        # -2 because we want first parent index and not it's position
        first_parent = (len(array) - 2) // 2
        
        # reversed because, that will lead to O(n) Time
        # Because, as we go up the parent nodes and sift them down
        # the subtrees will already follow the maxheap property
        for current_idx in reversed(range(first_parent+1)):
            self.sift_down(current_idx)
            
    # sift the last node up to it's correct position
    # O(log(n))
    def sift_up(self):
        child_idx   = len(self.heap)-1
        parent_idx  = (len(self.heap)-1)//2
        
        # as long as parent idx is greater than or equal to root
        # we can check
        while parent_idx >= 0:
            if self.heap[parent_idx] < self.heap[child_idx]:
                self.swap(parent_idx, child_idx)
                child_idx   = parent_idx
                parent_idx  = (child_idx-1)//2
            else:
                break
                
    # sifts the given node index down to it's correct position
    # O(log(n))
    def sift_down(self, node_idx):
        endidx      = len(self.heap)-1
        child_one   = (2 * node_idx ) + 1
        
        while child_one <= endidx:
            child_two = (2 * node_idx) + 2 if (2 * node_idx) + 2 <= endidx else None
            
            if child_two is not None:
                if self.heap[child_one] > self.heap[child_two]:
                    to_compare_with = child_one
                else:
                    to_compare_with = child_two
            else:
                to_compare_with = child_one
                
            if self.heap[node_idx] < self.heap[to_compare_with]:
                self.swap(node_idx, to_compare_with)
                node_idx    = to_compare_with
                child_one   = (2 * node_idx) + 1
            else:
                break
                
    # get the largest element
    def peek(self):
        return self.heap[0]
    
    # remove and retrieve the largest element
    def remove(self):
        self.swap(0, len(self.heap)-1)
        maximum_ele = self.heap.pop()
        self.sift_down(0)
        return maximum_ele
    
    # insert into heap
    def insert(self, value):
        self.heap.append(value)
        self.sift_up()
        
    # helper function
    def swap(self, x, y):
        self.heap[x], self.heap[y] = self.heap[y], self.heap[x]
        
    # returns heap in string format
    def __str__(self):
        return str(self.heap)
    
    # returns the length of the heap
    def __len__(self):
        return len(self.heap)
    
    
# Quick Select Implementation
class QuickSelect:
    def __init__(self, array, position):
        self.smallest_idx   = position - 1
        self.largest_idx    = len(array) - position
        self.correct_idx    = None
        self.selected       = None
        self.select(0, len(array)-1, array, False)
        
        
    # Takes in 4 variables
    # start and end specify the window size of the quick select algorithm
    # array is the list on which quick select will be performed
    # if smallest is True the smallest element for the given position will be selected
    # otherwise the largest element for the given position will be selected
    def select(self, start, end, array, smallest=True):
        if smallest:
            self.correct_idx = self.smallest_idx
        else:
            self.correct_idx = self.largest_idx
        
        while True:
            left, right = start+1, end
            pivot       = array[start]

            while left <= right:
                if array[left] > pivot and array[right] < pivot:
                    self.swap(left, right, array)
                    left  += 1
                    right -= 1

                elif array[right] >= pivot:
                    right -= 1

                else:
                    left  += 1

            # put pivot in it's correct position
            self.swap(start, right, array)

            
            # if pivot was put in desired position
            # we selected the element we wanted
            # break
            if array[self.correct_idx] == pivot:
                self.selected = pivot
                break

            # pivot was put towards the right of the desired index
            # which implies that all the elements towards the right-side of the pivot index i.e right, will be greater than the pivot
            # our desired element must be smaller than pivot as pivot is in it's correct position and is towards right of the desired index
            # we can eliminate the right part, as it cannot contain our desired element
            if right > self.correct_idx:
                start, end = 0, right -1
            else:
                # similarly we can eliminate the left part
                start, end = right + 1, len(array)-1
                
                    
    def swap(self, x, y, array):
        array[x], array[y] = array[y], array[x]

        

class Solution:
    # Using Quick Select Algorithm
    # O(n) Time (Average) and O(1) Space
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if k == len(nums): return min(nums)
        if k == 1        : return max(nums)
        
        return QuickSelect(nums, k).selected
        
    # Using Max Heap
    # O(n) Time (Average) and O(n) Space
    def findKthLargest_heap(self, nums: List[int], k: int) -> int:
        heap = MaxHeap(nums)
        
        for _ in range(k-1):
            heap.remove()
            
        return heap.remove()
        

# Kunal Wadhwa
