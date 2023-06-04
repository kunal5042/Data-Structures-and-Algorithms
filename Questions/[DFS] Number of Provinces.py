# Question: https://leetcode.com/problems/number-of-provinces/description/
# Medium

from typing import List

class Solution:
    def dfs(self, node, is_connected, visited):
        visited.add(node)
        for idx in range(len(is_connected)):
            if is_connected[node][idx] == 1 and idx not in visited:
                self.dfs(idx, is_connected, visited)

    # O(n*n) time and O(n) space
    def findCircleNum(self, is_connected: List[List[int]]) -> int:
        nodes = len(is_connected)
        number_of_components = 0
        visited = set()

        for idx in range(nodes):
            if idx not in visited:
                number_of_components += 1
                self.dfs(idx, is_connected, visited)

        return number_of_components


# June 04, 2023

'''

# Kunal Wadhwa

'''