# Question: https://leetcode.com/problems/knight-dialer/description/?envType=daily-question&envId=2023-11-27
# Knight Dialer

from collections import deque
from functools import cache

class Solution:
    def __init__(self):
        self.graph = {
                1:[8,6], 2:[7,9], 3:[4,8],
                4:[3,9,0], 5:[], 6:[1,0,7],
                7:[2,6], 8:[1,3], 9:[2,4],
                0:[4,6]
            }

        self.mod = (10**9) + 7

    # brute force solution
    def knightDialer(self, n: int) -> int:
        if n == 0: return 0
        dp = self.graph
        distinct_numbers = 0

        for idx in range(10):
            x = n - 1
            queue = deque([idx])

            while x != 0 and len(queue) != 0:
                count = len(queue)

                for _ in range(count):
                    step = queue.popleft()
                    for delta in dp[step]:
                        queue.append(delta)

                x -= 1

            distinct_numbers +=  len(queue) % self.mod

        return distinct_numbers

    # bottom up dynamic programming
    def knightDialer(self, n: int) -> int:
        @cache
        def get_paths(steps_allowed, square):
            if steps_allowed == 0:
                return 1
            
            paths = 0
            for next_square in self.graph[square]:
                paths = (paths + get_paths(steps_allowed-1, next_square)) % self.mod
            return paths

        result = 0
        for idx in range(10):
            result = (
                result + get_paths(n-1, idx)
            ) % self.mod
        
        return result

        


# November 27, 2023

'''

# Kunal Wadhwa

'''