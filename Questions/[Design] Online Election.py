# Question: https://leetcode.com/problems/online-election/
# Medium
from typing import Optional, List

from bisect import bisect_left
class Person:
    def __init__(self, id, time):
        self.id = id
        self.time = time
        self.votes = 0
        
class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.votes = persons
        self.timestamps = times
        self.candidates = {}
        self.winners = [None for _ in range(len(persons))]
        self.leader = None
        self.stamp_to_index = {stamp:idx for idx, stamp in enumerate(times)}
        self.initialize()
        
    # O(n) time and O(n) space
    def initialize(self):
        idx = 0
        for cand, time in zip(self.votes, self.timestamps):
            if cand not in self.candidates:
                self.candidates[cand] = Person(cand, time)
            
            self.candidates[cand].votes += 1
            self.candidates[cand].time = time
            
            if self.leader is None:
                self.leader = self.candidates[cand]
                
            if self.candidates[cand].votes > self.leader.votes:
                self.leader = self.candidates[cand]

            elif self.candidates[cand].votes == self.leader.votes:
                if self.candidates[cand].time > self.leader.time:
                    self.leader = self.candidates[cand]
                    
            self.winners[idx] = self.leader.id
            idx += 1

    # O(log(n)) time and O(n) space
    def q(self, t: int) -> int:
        if t in self.stamp_to_index:
            return self.winners[self.stamp_to_index[t]]
        
        idx = bisect_left(self.timestamps, t)
        
        if idx == len(self.winners):
            return self.winners[~0]
        
        return self.winners[idx-1]


# November 19, 2022

'''

# Kunal Wadhwa

'''