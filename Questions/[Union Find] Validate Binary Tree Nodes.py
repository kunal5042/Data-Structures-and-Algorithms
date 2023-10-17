# Question: https://leetcode.com/problems/validate-binary-tree-nodes/
# Medium

class UnionFind:
    def __init__(self, n):
        self.components = n
        self.parents = list(range(n))
        
    def union(self, parent, child):
        parent_parent = self.find(parent)
        child_parent = self.find(child)
        
        if child_parent != child or parent_parent == child_parent:
            return False
        
        self.components -= 1
        self.parents[child_parent] = parent_parent
        return True

    def find(self, node):
        if self.parents[node] != node:
            self.parents[node] = self.find(self.parents[node])
        
        return self.parents[node]
        

from typing import List

class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        uf = UnionFind(n)
        for node in range(n):
            for child in [leftChild[node], rightChild[node]]:
                if child == -1:
                    continue

                if not uf.union(node, child):
                    return False
                
        return uf.components == 1


# October 17, 2023

'''

# Kunal Wadhwa

'''