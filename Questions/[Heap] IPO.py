# Question: https://leetcode.com/problems/ipo/
# Hard
from typing import Optional, List

class Solution:
    # O(n*log(n)) time and O(n) space
    def findMaximizedCapital(self, max_projects: int, global_capital: int, profits: List[int], capitals_required: List[int]) -> int:
        available = []
        projects = [(profit, capital) for profit, capital in zip(profits, capitals_required)]
        projects.sort(key=lambda x: x[1])
        pointer = 0
        
        while max_projects > 0:
            while pointer < len(projects) and projects[pointer][1] <= global_capital:
                profit, capital = projects[pointer]
                heappush(available, (-profit, capital))
                pointer += 1
                
            if len(available) == 0: break
            global_capital += abs(heappop(available)[0])
            max_projects -=1
            
        return global_capital
                


# December 29, 2022

'''

# Kunal Wadhwa

'''