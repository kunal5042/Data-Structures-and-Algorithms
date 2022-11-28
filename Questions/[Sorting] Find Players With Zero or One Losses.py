# Question: https://leetcode.com/problems/find-players-with-zero-or-one-losses/
# Medium
from typing import Optional, List

class Solution:
    # O(n*log(n)) time and O(n) space
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        _hash = {}
        
        for winner, loser in matches:
            if not winner in _hash:
                _hash[winner] = 0
            
            if not loser in _hash:
                _hash[loser] = 0
                
            _hash[loser] += 1
                
        undefeated = []
        defeated_once = []
        
        for player, lost_matches in _hash.items():
            if lost_matches > 1:
                continue
                
            if lost_matches == 1:
                defeated_once.append(player)
                
            if lost_matches == 0:
                undefeated.append(player)
                
        return [sorted(undefeated), sorted(defeated_once)]
    
    # O(n+k) time and O(k) space: where k is the range of values in winner or loser
    # using the idea of counting sort
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        losses = [-1 for _ in range(10**5+1)]
        
        lower = float('inf')
        upper = float('-inf')
        for winner, loser in matches:
            if losses[winner] == -1:
                losses[winner] = 0
                
            if losses[loser] == -1:
                losses[loser] = 0
                
            losses[loser] += 1
            lower = min(lower, winner, loser)
            upper = max(upper, winner, loser)
            
        undefeated = []
        defeated_once = []
        
        for idx in range(int(lower), int(upper+1)):
            if losses[idx] == 0:
                undefeated.append(idx)
                
            if losses[idx] == 1:
                defeated_once.append(idx)
                
        return [undefeated, defeated_once]
                


# November 28, 2022

'''

# Kunal Wadhwa

'''