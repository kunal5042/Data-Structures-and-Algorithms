# Question: https://leetcode.com/problems/top-k-frequent-elements/

from typing import Optional, List
from collections import Counter
import heapq

class Solution:
    # Using a variation of Bucket-Sort Algorithm
    # O(n) Time and O(n) Space
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        bucket = [list() for _ in range(len(nums)+1)]
        for num, freq in counts.items():
            bucket[freq].append(num)
            
        result = list()
        for idx in reversed(range(len(bucket))):
            if len(result) == k: break
            while len(result) != k and len(bucket[idx]) != 0:
                result.append(bucket[idx].pop())
                
        return result
    
    
    # O( n + k * log(n)) Time and O(n) Space
    def topKFrequent_maxheap(self, nums: List[int], k: int) -> List[int]:
        counts  = Counter(nums)
        array   = [(freq, num) for num, freq in counts.items()]
        heap    = MaxHeap(array)
        largest = heap.largest(k)
        result  = [num for (freq, num) in largest]
        return result
    
    def topKFrequent_collections_counter(self, nums, k):
        counts  = Counter(nums)
        result  = [num for (num, freq) in counts.most_common(k)]
        
        return result
        
class MaxHeap:
    def __init__(self, array):
        heapq._heapify_max(array)
        self.heap = array
        self.len  = len(array)
        
    def pop(self):
        if self.len <= 0:
            return False
        self.len -= 1
        return heapq._heappop_max(self.heap)
    
    
    def largest(self, k):
        return heapq.nlargest(k, self.heap)
    
    def empty(self):
        return self.len <= 0

# Kunal Wadhwa
