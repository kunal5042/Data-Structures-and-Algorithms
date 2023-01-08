# Question: https://leetcode.com/problems/valid-square/
# Medium
from typing import Optional, List

class Solution:
    # O(1) time and O(1) space
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        def distance(A, B):
            x1, y1 = A
            x2, y2 = B
            return (y2 - y1) * (y2 - y1) + (x2 - x1) * (x2 - x1)
        
        points = sorted([p1, p2, p3, p4])
        c1 = distance(points[0], points[1]) != 0
        c2 = distance(points[0], points[1]) == distance(points[1], points[3])
        c3 = distance(points[1], points[3]) == distance(points[3], points[2])
        c4 = distance(points[3], points[2]) == distance(points[2], points[0])
        c5 = distance(points[0], points[3]) == distance(points[1], points[2])
        return all([c1, c2, c3, c4, c5])
    


# January 08, 2023

'''

# Kunal Wadhwa

'''