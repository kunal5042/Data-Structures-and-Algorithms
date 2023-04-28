# Question: https://leetcode.com/problems/similar-string-groups/
# Hard

from collections import defaultdict
from typing import List

class Solution:
    # O(n*n*m) time and O(n*n) space
    # where n = len(words) and m = len(max(words, key=len))
    def numSimilarGroups(self, words: List[str]) -> int:
        graph = defaultdict(set)
        visited = set()
        connected_components = 0

        def is_similar(word1, word2):
            difference = 0
            for idx in range(len(word1)):
                if word1[idx] != word2[idx]:
                    difference += 1

            return difference == 2 or difference == 0

        def build_graph():
            for idx in range(len(words)):
                for jdx in range(idx+1, len(words)):
                    if is_similar(words[idx], words[jdx]):
                        graph[words[idx]].add(words[jdx])
                        graph[words[jdx]].add(words[idx])

        def depth_first_pair(word):
            visited.add(word)
            for neighbor in graph[word]:
                if neighbor not in visited:
                    depth_first_pair(neighbor)

        build_graph()
        for word in words:
            if word in visited: continue
            depth_first_pair(word)
            connected_components += 1
            
        return connected_components


# April 28, 2023

'''

# Kunal Wadhwa

'''