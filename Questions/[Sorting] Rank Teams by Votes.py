# Question: https://leetcode.com/problems/rank-teams-by-votes/
# Medium
from typing import Optional, List

class Solution:
    # O(n* (n(log(n)))) time and O(n*n) Space
    def rankTeams(self, votes: List[str]) -> str:
        teams = {}
        
        for voting in votes:
            for idx, team in enumerate(voting):
                if team not in teams:
                    teams[team] = [0 for _ in range(len(votes[0]))]
                    
                teams[team][idx] += 1
        
        team_names = sorted(teams.keys())
        return "".join(sorted(team_names, key=lambda x:teams[x] , reverse=True))
'''

# Kunal Wadhwa

'''