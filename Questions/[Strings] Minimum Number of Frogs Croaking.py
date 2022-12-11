# Question: https://leetcode.com/problems/minimum-number-of-frogs-croaking/
# Medium
from typing import Optional, List

class Solution:
    # O(n^2) Time and O(n) Space
    def minNumberOfFrogs(self, croak_of_frogs: str) -> int:
        sound = {0:'c', 1:'r', 2:'o', 3:'a', 4:'k'}
        frogs = [0]
        
        for idx in range(len(croak_of_frogs)):
            new_frog = True
            
            for jdx, frog in enumerate(frogs):
                if sound[frog] == croak_of_frogs[idx]:
                    frogs[jdx] += 1
                    frogs[jdx] %= 5
                    new_frog = False
                    break
                    
            if new_frog is True:
                if croak_of_frogs[idx] == 'c':
                    frogs.append(1)
                else:
                    return -1
                
                
        for frog in frogs:
            if frog != 0: return -1
            
        return len(frogs)
    
    
    # Logic - maximum frogs required at once 
    def minNumberOfFrogs(self, croak_of_frogs: str) -> int:
        c, r, o, a, k = 0, 0, 0, 0, 0
        frogs, result = 0, 0
        
        for sound in croak_of_frogs:
            if sound == 'c':
                # new frog or existing one
                c += 1
                frogs += 1
                
            elif sound == 'r': r += 1
            elif sound == 'o': o += 1
            elif sound == 'a': a += 1
            
            elif sound == 'k':
                # free a frog
                k += 1
                frogs -= 1
                
            if c < r or r < o or o < a or a < k: return -1
                
            result = max(result, frogs)
            
        if c == r == o == a == k and frogs == 0: return result
        return -1
'''

# Kunal Wadhwa

'''