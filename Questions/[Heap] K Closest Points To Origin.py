# Question: https://leetcode.com/problems/k-closest-points-to-origin/

from typing import Optional, List
from functools import cmp_to_key as cmp
import heapq as heap

class Solution:
    # Using MinHeap
    # O(n) Time and O(n) Space
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def distance(p1):
            x1, y1 = p1
            return (x1)**2 + (y1)**2
        
        for idx in range(len(points)):
            points[idx] = (distance(points[idx]), points[idx])
            
        heap.heapify(points)
        result = [point for distance, point in heap.nsmallest(k, points)]
        return result
    
    # O(n log(n)) Time and O(n) Space
    def kClosest_sorting(self, points: List[List[int]], k: int) -> List[List[int]]:
        def distance(p1):
            x1, y1 = p1
            return (x1)**2 + (y1)**2
        
        for idx in range(len(points)):
            points[idx] = (points[idx], distance(points[idx]))
            
        points.sort(key=lambda x: x[1])
        result = list(map(lambda x: x[0], points))
        return result[:k]
            
    
    
    # O(n**2) Worst Time and O(1) Space
    def kClosest_bubble(self, points: List[List[int]], k: int) -> List[List[int]]:
        def comparator(p1, p2):
            x1, y1 = p1
            x2, y2 = p2
            
            d1 = (x1)**2 + (y1)**2
            d2 = (x2)**2 + (y2)**2
            
            if d1 > d2: return 1
            if d2 > d1: return -1
            return 0
        
        points.sort(key=cmp(comparator))
        
        return points[:k]

# Kunal Wadhwa
