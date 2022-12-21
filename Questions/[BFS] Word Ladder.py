# Question: https://leetcode.com/problems/word-ladder/
# Hard
from typing import Optional, List
from collections import deque, defaultdict
from string import ascii_lowercase as alphabets

class Solution:
    # Accepted on LeetCode, but slow
    def ladderLength(self, begin_word: str, end_word: str, word_list: List[str]) -> int:
        queue = deque()
        queue.append((begin_word, 1))
        visited = set()
        word_list = set(word_list)
        
        while len(queue) != 0:
            word, seq_length = queue.popleft()
            
            if word in visited: continue
            visited.add(word)
            
            # shortest path reaches first
            if word == end_word: return seq_length
            
            # the idea is to generate every possible mutant of the given word
            # and check if the mutant is present in the word_list
            # follow all possible paths
            # shortest path reaches the end_word first, nature of BFS using queue
            
            for idx in range(len(word)):
                exclude_idx = alphabets.find(word[idx])
                
                for jdx in range(26):
                    if jdx == exclude_idx: continue
                    mutation = word[:idx] + alphabets[jdx] + word[idx+1:]
                    
                    if mutation not in visited and mutation in word_list:
                        queue.append((mutation, seq_length+1))
        return 0

    # Faster than previous solution
    def ladderLength(self, begin_word: str, end_word: str, word_list: List[str]) -> int:
        mutations = defaultdict(list)
        word_list.append(begin_word)

        # the idea is to generate all possible mutant templates from the words in word_list
        # create a hash_map where key = mutant template and value = words in word_list which fit this template
        for word in word_list:
            for idx in range(len(word)):
                mutations[word[:idx] + '*' + word[idx+1:]].append(word)
                
        queue = deque([begin_word])
        visited = set()
        sequence_length = 1
        
        while len(queue) != 0:
            nodes = len(queue)
            
            for _ in range(nodes):
                word = queue.popleft()
                
                if word in visited: continue
                visited.add(word)
                
                # shortest path reaches first
                if word == end_word: return sequence_length
                
                # check which mutants can the current word form
                # using the pre-calculated hash_map
                # this avoids generating all mutants and checking their presence in the word_list
                for idx in range(len(word)):
                    mutant_template = word[:idx] + '*' + word[idx+1:]
                    for mutant in mutations[mutant_template]:
                        if mutant not in visited:
                            queue.append(mutant)
                            
            sequence_length += 1
            
        return 0


# December 21, 2022

'''

# Kunal Wadhwa

'''