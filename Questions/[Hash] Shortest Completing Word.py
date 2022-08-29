# Question: https://leetcode.com/problems/shortest-completing-word/
# Easy
# 0.0
from typing import Optional, List

from collections import Counter
from string import digits

class Solution:
    def shortestCompletingWord(self, license_plate: str, words: List[str]) -> str:
        """Takes a target string and a list of strings
        Finds and returns the shortest string in the list that,
        can complete the target string
        """
        plate_chars   = Counter(filter(lambda x: x.isalpha(), license_plate.lower()))
        shortest_word = None
        
        for word in words:
            word_chars = Counter(word)
           
            # bit-wise AND
            if plate_chars == (word_chars & plate_chars):
                shortest_word = min(shortest_word, word, key=len) \
                if shortest_word is not None else word
                
        return shortest_word
'''

# Kunal Wadhwa

'''