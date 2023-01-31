# Question: https://leetcode.com/problems/generate-random-point-in-a-circle/
# Medium

import random
from typing import List

class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.radius = radius
        self.x_center = x_center
        self.y_center = y_center
        
    def is_inside(self, x1, y1):
        distance = (self.x_center - x1)**2 + (self.y_center - y1)**2
        return distance <= self.radius**2

    def randPoint(self) -> List[float]:
        while True:
            x = random.uniform(self.x_center-self.radius, \
                               self.x_center+self.radius)
            y = random.uniform(self.y_center-self.radius, \
                               self.y_center+self.radius)
            
            if self.is_inside(x, y):
                return [x, y]


# January 31, 2023

'''

# Kunal Wadhwa

'''