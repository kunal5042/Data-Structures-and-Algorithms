# Question: https://leetcode.com/problems/beautiful-arrangement/
# Medium
# To Do: Solve using DP
from typing import Optional, List

class Solution:
    # O(n*n!) Time
    def countArrangement(self, n: int) -> int:
        # serves two purpose
        # i value represents the number
        # visited[i] is a bool value representing if the number i
        # has been used in the current permutation or not
        visited = [False for _ in range(n+1)]
        
        # keep track of beautiful arrangements
        count = 0
        
        def solve(idx, perm):
            nonlocal count
            if perm == n:
                # we reached here, means
                # we found a beautiful arrangement of length n
                count += 1
                return
            
            for num in range(1, len(visited)):
                if visited[num] is False:
                    if idx % num == 0 or num % idx == 0:
                        visited[num] = True
                        # move ahead in this permutation
                        solve(idx + 1, perm + 1)
                        # backtrack
                        visited[num] = False
        
        solve(1, 0)
        return count

'''

# Kunal Wadhwa

'''