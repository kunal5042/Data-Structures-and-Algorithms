# Question: https://leetcode.com/problems/word-break-ii/
# Hard

class Trie:
    def __init__(self):
        self.end_symbol = "$"
        self.root = {}

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node:
                node[char] = {}
            node = node[char]
        node[self.end_symbol] = True

    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if char not in node:
                return False
            node = node[char]
        return self.end_symbol in node

    def starts_with(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            if char not in node:
                return False
            node = node[char]
        return True

from typing import List

class Solution:
    # accepted on leetcode
    def wordBreak(self, characters: str, word_dict: List[str]) -> List[str]:
        paths = []
        
        def segment(idx, path):
            if idx >= len(characters):
                paths.append(" ".join(path))
                return
            
            trie = Trie()
            trie.insert(characters[idx:])
            for word in word_dict:
                if trie.starts_with(word):
                    path.append(word)
                    segment(idx+len(word), path)
                    path.pop()
        
        segment(0, [])
        return paths
    
    # more optimal approach
    def wordBreak(self, characters: str, word_dict: List[str]) -> List[str]:
        paths = []
        trie = Trie()
        for word in word_dict:
            trie.insert(word)

        def segment(idx, path):
            if idx >= len(characters):
                paths.append(" ".join(path))
                return

            current_node = trie.root
            for jdx in range(idx, len(characters)):
                if characters[jdx] not in current_node:
                    return

                current_node = current_node[characters[jdx]]

                if trie.end_symbol in current_node:
                    path.append(characters[idx:jdx+1])
                    segment(jdx+1, path)
                    path.pop()
                    
        segment(0, [])
        return paths


# May 01, 2023

'''

# Kunal Wadhwa

'''