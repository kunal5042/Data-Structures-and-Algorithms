# Question: https://leetcode.com/problems/number-of-ways-to-divide-a-long-corridor/description/?envType=daily-question&envId=2023-11-28
# Hard

from functools import cache

class Solution:
    def __init__(self):
        self.array = []
        self.mod = (10**9) + 7

    @cache
    def calculate_ways(self, idx, seats):
        if idx == len(self.array):
            if seats == 2: return 1
            return 0
        
        element = self.array[idx]

        if element == 'S':
            updated_seats = 1 if seats + 1 > 2 else seats + 1
            return self.calculate_ways(idx+1, updated_seats)
        
        y = 0
        if seats == 2:
            y = self.calculate_ways(idx+1, 0)

        return y + self.calculate_ways(idx+1, seats) 

    def numberOfWays(self, corridor: str) -> int:
        self.array = corridor
        return self.calculate_ways(0, 0) % self.mod

    def numberOfWays(self, corridor: str) -> int:
        seat=[i for i in range(len(corridor)) if corridor[i]=='S']
        if len(seat) % 2 != 0 or len(seat)==0:
            return 0
        ans=1
        for i in range(1,len(seat)-2,2):
            ans *= (seat[i+1] - seat[i])
        return ans % self.mod


# November 29, 2023

'''

# Kunal Wadhwa

'''