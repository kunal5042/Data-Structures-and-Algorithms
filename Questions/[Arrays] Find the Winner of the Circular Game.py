# Question: https://leetcode.com/problems/find-the-winner-of-the-circular-game/
# Medium
from typing import Optional, List

class Solution:
    # O(n*k) time and O(n) space
    def findTheWinner(self, n: int, k: int) -> int:
        players = deque([idx for idx in range(1, n+1)])
        
        while len(players) != 1:
            pool = k
            while pool > 0:
                players.append(players.popleft())
                pool -= 1
                
            players.pop()
            
        return players.popleft()


# January 16, 2023

'''

# Kunal Wadhwa

'''