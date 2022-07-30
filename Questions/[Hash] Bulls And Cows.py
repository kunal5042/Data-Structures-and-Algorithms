# Question: https://leetcode.com/problems/bulls-and-cows/

from typing import Optional, List

from collections import Counter
class Solution:
    # O(n) Time and O(n) Space
    def getHint(self, secret: str, guess: str) -> str:
        bulls, cows = 0, 0
        counts_secret, counts_guess = Counter(secret), Counter(guess)
        
        for idx in range(len(secret)):
            if secret[idx] == guess[idx]:
                counts_secret[secret[idx]] -= 1
                counts_guess[guess[idx]] -= 1
                bulls += 1
                
        
        for char, freq in counts_secret.items():
            if freq > 0:
                freq_guess = counts_guess[char]
                
                if freq_guess > freq:
                    cows += freq
                else:
                    cows += freq_guess
                    
                    
        return str(bulls) + 'A' + str(cows) + 'B'
'''

# Kunal Wadhwa

'''