# Question: https://leetcode.com/problems/dota2-senate/
# Medium

from collections import defaultdict

class Solution:
    # O(n) time and O(n) space
    def predictPartyVictory(self, senate: str) -> str:
        can_vote = [True for _ in range(len(senate))]
        indices = defaultdict(list)
        flip = lambda party: 'R' if party == 'D' else 'D'
            
        bans_collected_R = bans_collected_D = 0
        while True:
            D = R = 0
            for idx in reversed(range(len(senate))):
                if can_vote[idx] is False: continue
                party = senate[idx]
                indices[party].append(idx)
                D += 1 if party == 'D' else 0
                R += 1 if party == 'R' else 0
            
            for idx, party in enumerate(senate):
                if can_vote[idx] is False: continue
                if party == 'D' and bans_collected_R > 0:
                    can_vote[idx] = False
                    bans_collected_R -= 1
                    D -= 1
                    if D == 0: return 'Radiant'
                    continue
                    
                if party == 'R' and bans_collected_D > 0:
                    can_vote[idx] = False
                    bans_collected_D -= 1
                    R -= 1
                    if R == 0: return 'Dire'
                    continue
                
                opposition = indices[flip(party)]

                while len(opposition) != 0 and opposition[~0] < idx:
                    opposition.pop()
                    
                if len(opposition) != 0:
                    can_vote[opposition.pop()] = False
                    
                    if flip(party) == 'D': D -= 1
                    if flip(party) == 'R': R -= 1
                else:
                    if party == 'D': bans_collected_D += 1
                    if party == 'R': bans_collected_R += 1
                    
                if R == 0: return 'Dire'
                if D == 0: return 'Radiant'
        


# January 31, 2023

'''

# Kunal Wadhwa

'''