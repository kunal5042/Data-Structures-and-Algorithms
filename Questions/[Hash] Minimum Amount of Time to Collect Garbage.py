# Question: https://leetcode.com/problems/minimum-amount-of-time-to-collect-garbage/
# Medium
#
from typing import Optional, List

from collections import Counter
class Solution:
    # O(n) Time and O(n) Space
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        metal = paper = glass = 0
        time  = 0
        
        counts = Counter(garbage[0])
        metal += counts['M']
        paper += counts['P']
        glass += counts['G']
        
        last_metal = last_paper = last_glass = 0
        fm = fp = fg = False
        for idx in reversed(range(len(garbage))):
            counts = set(garbage[idx])
            if 'M' in counts and fm is False:
                fm = True
                last_metal = idx
            if 'G' in counts and fg is False:
                fg = True
                last_glass = idx
            if 'P' in counts and fp is False:
                fp = True
                last_paper = idx
                
            if fm is True and fp is True and fg is True:
                break
        
        tm = tg = tp = 0
        for idx in range(1, len(garbage)):
            counts = Counter(garbage[idx])
            metal += counts['M']
            paper += counts['P']
            glass += counts['G']
            if idx <= last_metal: tm += travel[idx-1]
            if idx <= last_paper: tp += travel[idx-1]
            if idx <= last_glass: tg += travel[idx-1]
                
        total = tm + metal + tp + paper + tg + glass
        return total
'''

# Kunal Wadhwa

'''