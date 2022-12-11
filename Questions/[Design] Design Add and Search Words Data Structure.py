# Question: https://leetcode.com/problems/design-add-and-search-words-data-structure/
# Medium
from typing import Optional, List

class WordDictionary:

    def __init__(self):
        self.root = {}
        self.end_symbol = '*'

    # trie insert
    def addWord(self, word: str) -> None:
        current_node = self.root
        for idx in range(len(word)):
            if word[idx] not in current_node:
                current_node[word[idx]] = {}
                
            current_node = current_node[word[idx]]
            
        current_node[self.end_symbol] = {}

    def search(self, word: str) -> bool:
        def helper(idx, word, node):
            if idx == len(word):
                return self.end_symbol in node
            
            if word[idx] != '.':
                if word[idx] not in node:
                    return False
                return helper(idx+1, word, node[word[idx]])
            
            else:
                # explore all paths where '.' is replaced with key
                for key in node:
                    # if any path returns True
                    if helper(idx+1, word, node[key]) is True:
                        return True
                return False
        
        return helper(0, word, self.root)

'''

# Kunal Wadhwa

'''