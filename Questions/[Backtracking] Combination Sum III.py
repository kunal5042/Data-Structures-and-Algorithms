# Question: https://leetcode.com/problems/combination-sum-iii/
# Medium
from typing import Optional, List

class Solution:
    # O(9! K/ (K-9)!) Time and O(K) Space 
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        combinations = []
        
        def compute(num, csum, path):
            if csum == n and len(path) == k:
                combinations.append(path.copy())
                return
            
            if csum > n or len(path) > k: return
            
            for next_num in range(num, 10):
                if csum + next_num <= n:
                    path.append(next_num)
                    compute(next_num+1, csum+next_num, path)
                    path.pop()
                    
        compute(1, 0, [])
        return combinations
'''

# Kunal Wadhwa

'''