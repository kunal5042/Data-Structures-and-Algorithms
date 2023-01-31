# Question: https://leetcode.com/problems/best-team-with-no-conflicts/
# Medium

from functools import cache
from typing import List

class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        pairs = []
        for score, age in zip(scores, ages):
            pairs.append((age, score))
            
        pairs.sort()
        
        @cache
        def maximum_score(idx, youngest_p, youngest_s):
            if idx == len(pairs):
                return 0
            
            max_score = include_score = exclude_score = 0
            age, score = pairs[idx]
            
            if age == youngest_p or (age > youngest_p and score >= youngest_s):
                # take the current player in team
                include_score = score + maximum_score(
                    idx + 1,
                    max(youngest_p, age),
                    max(youngest_s, score)
                )
                
            # don't take the current player in team
            exclude_score = maximum_score(
                idx + 1,
                youngest_p,
                youngest_s
            )
                
            max_score = max(include_score, exclude_score)
            
            return max_score
        
        return maximum_score(0, -1, -1)
    
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        pairs = []
        for score, age in zip(scores, ages):
            pairs.append((age, score))
            
        pairs.sort(reverse=True)
        
        max_score = 0
        dp = [0 for _ in range(len(pairs))]
        
        for idx in range(len(pairs)):
            score = pairs[idx][1]
            dp[idx] = score

            for jdx in range(idx):
                if pairs[jdx][1] >= pairs[idx][1]:
                    dp[idx] = max(dp[idx], dp[jdx] + score)
                    
            max_score = max(max_score, dp[idx])
            
        return max_score


# January 31, 2023

'''

# Kunal Wadhwa

'''