# Question: https://leetcode.com/problems/implement-trie-prefix-tree/
# Medium
from typing import Optional, List

class Trie:

    def __init__(self):
        self.root = {}
        self.end_symbol = '*'

    # O(len(word)) Time and O(len(word)) Space
    def insert(self, word: str) -> None:
        current_node = self.root

        for idx in range(len(word)):
            if word[idx] not in current_node:
                current_node[word[idx]] = {}
                    
            current_node = current_node[word[idx]]
                
        current_node[self.end_symbol] = True

    # O(len(word)) Time
    def search(self, word: str) -> bool:
        trie = self.root
        for idx in range(len(word)):
            if word[idx] not in trie:
                return False
            trie = trie[word[idx]]
            
        return self.end_symbol in trie

    # O(len(prefix)) Time
    def startsWith(self, prefix: str) -> bool:
        trie = self.root
        for idx in range(len(prefix)):
            if prefix[idx] not in trie:
                return False
            trie = trie[prefix[idx]]
            
        return True
'''

# Kunal Wadhwa

'''