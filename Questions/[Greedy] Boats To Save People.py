# Question: https://leetcode.com/problems/boats-to-save-people/

from typing import Optional, List

class Solution:
    # O(n) Time and O(1) Space
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        lightest, heaviest = 0, len(people) - 1
        people.sort()
        boats = 0
        
        while lightest <= heaviest:
            if people[lightest] + people[heaviest] > limit:
                heaviest -= 1
                
            else:
                # greedy
                lightest += 1
                heaviest -= 1
                
            boats += 1
          
        return boats
'''

# Kunal Wadhwa

'''