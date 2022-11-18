# Question: https://leetcode.com/problems/finding-the-users-active-minutes/
# Medium
from typing import Optional, List

class Solution:
    # O(n) time and O(n) space
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        output = [0 for _ in range(k)]
        data = defaultdict(set)
        
        for userid, time in logs:
            data[userid].add(time)
            
        for UAM in data.values():
            if len(UAM) <= k: output[len(UAM)-1] += 1
                
        return output
'''

# Kunal Wadhwa

'''