# Question: https://leetcode.com/problems/shifting-letters-ii/
# Medium
from typing import Optional, List

from string import ascii_lowercase
class Solution:
    # Brute Force
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        chars   = {idx   : char for idx, char in enumerate(ascii_lowercase)}
        indices = {char  : idx  for idx, char in enumerate(ascii_lowercase)}
        
        # change the state as the changes are being made
        state = [0 for _ in range(len(s))]
        
        for idx in range(len(shifts)):
            start, end, direction = shifts[idx]
            offset = 1 if direction == 1 else -1
            
            for jdx in range(start, end+1):
                state[jdx] += offset
                state[jdx] %= 26
                
        # generate string using the final state
        for idx in range(len(state)):
            state[idx] = chars[(indices[s[idx]] + state[idx]) % 26]
            
        return "".join(state)
    
    
    # O(m) Time and O(n) Space - where m and n are the length of shifts array and string respectively
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        chars   = {idx   : char for idx, char in enumerate(ascii_lowercase)}
        indices = {char  : idx  for idx, char in enumerate(ascii_lowercase)} 
        ranges  = [0 for idx in range(len(s)+1)]
        
        # mark the start and the end indices according to the change that needs to be made
        for start, end, direction in shifts:
            if direction == 1:
                # move ahead from start till end
                ranges[start] += 1
                ranges[end+1] -= 1
            else:
                # move back from start till end
                ranges[start] -= 1
                ranges[end+1] += 1

        # prefix-sum will mark the changes for all indices
        for idx in range(1, len(ranges)):
            ranges[idx] += ranges[idx-1]

        # generate final string
        result = []
        for idx in range(len(ranges)-1):
            result.append(chars[(indices[s[idx]] + ranges[idx]) % 26])
            
        return "".join(result)
'''

# Kunal Wadhwa

'''