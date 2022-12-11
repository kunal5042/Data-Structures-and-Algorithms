# Question: https://leetcode.com/problems/open-the-lock/
# Medium
from typing import Optional, List

from collections import deque
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if target == '0000': return 0
        queue         = deque(['0000'])
        deadend       = set(deadends)
        target_int    = int(target)
        visited       = set()
        minimum_moves = 0
        
        def turn_both_sides(idx, string):
            integer = int(string[idx])
            increment = (integer + 1) % 10
            decrement = integer - 1 if integer != 0 else 9
            forward = string[:idx] + str(increment) + string[idx+1:]
            backward = string[:idx] + str(decrement) + string[idx+1:]
            return forward, backward
        
        while len(queue) != 0:
            minimum_moves += 1
            level_breadth = len(queue)
            
            for _ in range(level_breadth):
                combination = queue.popleft()

                if combination in visited or combination in deadend:
                    continue
                    
                visited.add(combination)
                for idx in range(4):
                    forward, backward = turn_both_sides(idx, combination)
                    if forward == target or backward == target: return minimum_moves
                    if forward  not in visited and forward  not in deadends: queue.append(forward)
                    if backward not in visited and backward not in deadends: queue.append(backward)
                
        return -1
'''

# Kunal Wadhwa

'''