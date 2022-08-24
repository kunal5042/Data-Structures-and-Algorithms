# Question: https://leetcode.com/problems/maximum-number-of-groups-entering-a-competition/
# Medium
from typing import Optional, List

class Solution:
    # Time-Limit Exceeded
    # Recursive Solution
    def maximumGroups(self, grades: List[int]) -> int:
        max_groups = 0
        grades.sort()
        
        def maximize_groups(start, groups, strength, score):
            if start == len(grades):
                nonlocal max_groups
                max_groups = max(max_groups, groups)
                return
            
            # pruning
            if len(grades) - start <= strength:
                return
            
            current_score = 0
            current_strength = 0
            for index in range(start, len(grades)):
                current_score += grades[index]
                current_strength += 1
                if current_strength > strength and current_score > score:
                    maximize_groups(index+1, groups+1, current_strength, current_score)
                    
        maximize_groups(0, 0, 0, 0)
        return max_groups
    
    # Greedy Approach
    # O(n) Time and O(1) Space
    def maximumGroups(self, grades: List[int]) -> int:
        max_groups = 0
        grades.sort()
        
        groups = 1
        strength, score = 1, grades[0]
        
        cur_strength, cur_score = 0, 0
        
        idx = 1
        while idx < len(grades):
            cur_score += grades[idx]
            cur_strength += 1
            
            if cur_score > score and cur_strength > strength:
                groups += 1
                strength, score = cur_strength, cur_score
                cur_score    = 0
                cur_strength = 0
            
            idx += 1
            
        return groups
'''

# Kunal Wadhwa

'''