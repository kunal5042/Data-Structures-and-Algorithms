# Question: https://leetcode.com/problems/expressive-words/
# Medium

from typing import List

class Solution:
    #
    # O(n*w) time and O(w) space
    # where
    # n = length of the words array
    # w = length of the longest word
    #
    def expressiveWords(self, s: str, words: List[str]) -> int:
        def split(word):
            buffer = word[0]
            buffer_length = 1
            result = []
            
            for idx in range(1, len(word)):
                if buffer != word[idx]:
                    result.append(buffer * buffer_length)
                    buffer = word[idx]
                    buffer_length  = 1
                else:
                    buffer_length += 1
                    
            this_split = buffer * buffer_length
            if len(result) == 0:
                result.append(this_split)
                
            if result[~0] != this_split:
                result.append(this_split)
            
            return result
        
        stretchy = 0
        target = split(s)
        for word in words:
            candidate = split(word)
            if len(candidate) != len(target):
                continue
            
            is_stretchy = True
            for idx in range(len(target)):
                target_split = target[idx]
                candid_split = candidate[idx]
                
                if target_split[0] != candid_split[0]:
                    is_stretchy = False
                    break
                    
                if len(target_split) == len(candid_split):
                    continue
                    
                if len(target_split) < len(candid_split) or \
                   len(target_split) < 3:
                    is_stretchy = False
                    break
                    
            stretchy += int(is_stretchy)
            
        return stretchy
                
            


# May 06, 2023

'''

# Kunal Wadhwa

'''