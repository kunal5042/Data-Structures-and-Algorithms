# Question: https://leetcode.com/problems/split-a-string-into-the-max-number-of-unique-substrings/
# Medium
# Backtracking with pruning
from typing import Optional, List

class Solution:
    # O(2^n) Time and O(n) Space
    def maxUniqueSplit(self, s: str) -> int:
        max_splits = float('-inf')
        path = set()
    
        def maximize_splits(start):
            nonlocal max_splits
            
            # pruning
            # removing those branches that can't lead to a result
            if len(s) - start + len(path) <= max_splits:
                # faster than 99.87 thanks to the line above
                return
            
            # successful path
            if start == len(s):
                max_splits = max(max_splits, len(path))
                return
            
            
            for idx in range(start + 1, len(s) + 1):
                if s[start : idx] not in path:
                    # explore this path further
                    path.add(s[start : idx])
                    
                    maximize_splits(idx)
                    
                    # remove this path
                    # and all the paths that we explored further from this path
                    # would have already been removed, because of the recursive nature
                    path.remove(s[start : idx])
                    
                    # we are ready to explore new paths
                    
        
        maximize_splits(0)
        return max_splits
'''

# Kunal Wadhwa

'''
