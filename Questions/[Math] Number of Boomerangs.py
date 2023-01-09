# Question: https://leetcode.com/problems/number-of-boomerangs/
# Medium
from typing import Optional, List

class Solution:
    # O(n*n) time and O(n) space
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        def distance(p1, p2):
            x1, y1 = p1
            x2, y2 = p2
            return (x2-x1)**2 + (y2-y1)**2
        
        boomerangs = 0
        for idx in range(len(points)):
            distances = defaultdict(int)
            
            for jdx in range(len(points)):
                this_distance = distance(points[idx], points[jdx])
                distances[this_distance] += 1
                
            for dist in distances:
                boomerangs += distances[dist] * (distances[dist]-1)
                
        return boomerangs


# January 09, 2023

'''

# Kunal Wadhwa

'''