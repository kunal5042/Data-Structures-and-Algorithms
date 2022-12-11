# Question: https://leetcode.com/problems/find-the-highest-altitude/
# Easy
#
from typing import Optional, List


class Solution:
    # O(n) Time and O(1) Space
    def largestAltitude(self, gain: List[int]) -> int:
        highest_altitude = max(0, gain[0])
        previous_altitude = gain[0]
        
        for idx in range(1, len(gain)):
            highest_altitude = max(previous_altitude + gain[idx], highest_altitude)
            previous_altitude += gain[idx]
            
        return highest_altitude
'''

# Kunal Wadhwa

'''