# Question: https://leetcode.com/problems/unique-binary-search-trees/
# Medium
from typing import Optional, List

class Solution:
    # O(n*n) Time and O(n) Space
    def numTrees(self, n: int) -> int:
        # every index of this 0-based array
        # stores the number of trees that can be formed
        # for number of nodes equal to the index
        num_trees = [0 for _ in range(n+1)]
        # base case
        num_trees[0] = 1
        
        for nodes_count in range(1, n+1):
            # stores the number of possible unique trees
            # that can be formed with current node count
            unique_trees = 0
            for root_node in range(1, nodes_count+1):
                unique_trees += (num_trees[root_node - 1] * num_trees[nodes_count - root_node])
                
            # store the solution to sub-problem
            num_trees[nodes_count] = unique_trees
            
        return num_trees[n]

'''

# Kunal Wadhwa

'''