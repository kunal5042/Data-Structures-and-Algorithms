# Question: https://leetcode.com/problems/max-points-on-a-line/
# Hard
from typing import Optional, List

class Solution:
    # O(n*n) time and O(n) space
    def maxPoints(self, points: List[List[int]]) -> int:
        def get_slope(x1, y1, x2, y2):
            if x2 == x1: return float('inf')
            return (y2 - y1) / (x2 - x1)
        
        result = 1
        for idx in range(len(points)):
            slopes = defaultdict(int)
            x1, y1 = points[idx]
            
            for jdx in range(idx + 1, len(points)):
                x2, y2 = points[jdx]
                slope = get_slope(x1, y1, x2, y2)
                slopes[slope] += 1
                result = max(result, 1 + slopes[slope])
                
        return result
        


# January 08, 2023

'''

# Kunal Wadhwa

'''