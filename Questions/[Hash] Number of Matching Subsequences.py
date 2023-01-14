# Question: https://leetcode.com/problems/number-of-matching-subsequences/
# Medium
from typing import Optional, List

from string import ascii_lowercase
class Solution:
    # O(len(s) * len(words)) and O(len(words)) space
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        pointers = [0 for _ in range(len(words))]
        for char in s:
            for idx in range(len(words)):
                cword = words[idx]
                cidx  = pointers[idx]
                
                if cidx < len(cword) and cword[cidx] == char:
                    pointers[idx] += 1
                    
        result = 0
        for idx in range(len(words)):
            if pointers[idx] == len(words[idx]):
                result += 1
        return result
    
    # Theta(len(s)) time and O(len(words)) space
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        index = {char:idx for idx, char in enumerate(ascii_lowercase)}
        looking_for = [[] for _ in range(26)]
        for word in words: looking_for[index[word[0]]].append(word)
            
        result = 0
        for char in s:
            waiting_words = looking_for[index[char]]
            update = []
            for _ in range(len(waiting_words)):
                word = waiting_words.pop()
                if len(word) == 1:
                    result += 1
                    continue
                update.append(word[1:])
                
            while len(update) != 0:
                looking_for[index[update[~0][0]]].append(update.pop())
                
        return result
        


# January 14, 2023

'''

# Kunal Wadhwa

'''