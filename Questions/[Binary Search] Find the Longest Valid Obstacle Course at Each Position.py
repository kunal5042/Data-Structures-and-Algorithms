# Question: https://leetcode.com/problems/find-the-longest-valid-obstacle-course-at-each-position/
# Hard

import bisect
from typing import List

class Solution:
    # O(n*log(n)) time and O(n) space
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        output = [1 for _ in range(len(obstacles))]

        aux = []

        for jdx, height in enumerate(obstacles):
            idx = bisect.bisect_right(aux, height)

            if idx == len(aux):
                aux.append(height)
            else:
                aux[idx] = height
                
            output[jdx] = idx + 1

        return output


# May 07, 2023

'''

# Kunal Wadhwa

'''