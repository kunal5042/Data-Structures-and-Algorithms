# Question: https://leetcode.com/problems/maximum-matching-of-players-with-trainers/
# Medium
from typing import Optional, List

class Solution:
    # O(n * log(n)) Time and O(1) Space - where n is the length of longer of the two arrays
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        matches, jdx = 0, 0
        
        for idx in range(len(players)):                
            while jdx < len(trainers) and trainers[jdx] < players[idx]:
                jdx += 1
                
            if jdx >= len(trainers): break
                
            matches += 1
            jdx += 1
            
        
        return matches
'''

# Kunal Wadhwa

'''