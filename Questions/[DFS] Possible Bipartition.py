# Question: https://leetcode.com/problems/possible-bipartition/
# Medium
from typing import Optional, List

class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph = {idx+1: set() for idx in range(n)}
        group1 = set()
        group2 = set()
        visited = set()

        for person1, person2 in dislikes:
            graph[person1].add(person2)
            graph[person2].add(person1)
            
        def disliking_cycle_detection(node, parent, group_id):
            if node in visited: return False
            visited.add(node)
            if group_id == 1: group1.add(node)
            if group_id == 2: group2.add(node)
            child_group = 2 if group_id == 1 else 1
            
            for adjacent in graph[node]:
                if adjacent not in visited:
                    if disliking_cycle_detection(adjacent, node, child_group) is True:
                        return True

                elif adjacent != parent:
                    if (
                        group_id == 1 and adjacent in group1
                        or
                        group_id == 2 and adjacent in group2
                    ):
                        return True
                
            return False
        
        for person in range(1, n+1):
            if person not in visited:
                if disliking_cycle_detection(person, -1, 1) is True:
                    return False
                
        return True


# December 21, 2022

'''

# Kunal Wadhwa

'''