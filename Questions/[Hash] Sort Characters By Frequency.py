# Question: https://leetcode.com/problems/sort-characters-by-frequency/
# Medium
# To Do: Solve using Priority Queue ✅
from typing import Optional, List
from queue import PriorityQueue as priority
from collections import Counter
import heapq

class Solution:
    # Using hashmap
    # O(n log(n)) Time and O(n) Space
    def frequency_sort(self, s: str) -> str:
        counts = dict()
        
        for char in s:
            counts[char] = counts.get(char, 0) + 1

            
        pair = sorted(counts.items(), key=lambda x: x[1], reverse=True)
        
        result = ''
        
        for char, frequency in pair:
            for _ in range(frequency):
                result += char
            
        return result
    
    # Using MaxHeap
    # O(n) Time and O(n) Space
    def frequencySort(self, s: str) -> str:
        counts = Counter(s)
        array  = [(freq, char) for char, freq in counts.items()]
        heap   = MaxHeap(array)
        result = ''
        while not heap.empty():
            freq, char = heap.pop()
            for _ in range(freq):
                result += char
                
        return result
    
    
    # Using Priority Queue
    # O(n log(n)) Time and O(n) Space
    def frequency_sort_pq(self, s: str) -> str:
        result = ''
        pq = priority()
        counts = Counter(s)
        for key, value in counts.items():
            pq.put((value, key))
            
        while not pq.empty():
            freq, char = pq.get()
            for _ in range(freq):
                result = char + result
        
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
    
    def empty(self):
        return self.len <= 0
        

# Kunal Wadhwa
