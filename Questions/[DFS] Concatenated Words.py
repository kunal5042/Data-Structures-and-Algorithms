# Question: https://leetcode.com/problems/concatenated-words/
# Hard
from typing import Optional, List

class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        result = []
        words_dict = set(words)
        
        for word in words:
            words_dict.remove(word)
            
            if self.check(word, words_dict) is True:
                result.append(word)
                
            words_dict.add(word)
            
        return result
    
    def check(self, word, words_dict):
        if word in words_dict:
            return True
        
        for idx in range(len(word), 0, -1):
            if word[:idx] in words_dict and self.check(word[idx:], words_dict):
                return True
        return False


# January 28, 2023

'''

# Kunal Wadhwa

'''