# Question: https://leetcode.com/problems/data-stream-as-disjoint-intervals/
# Hard
from typing import Optional, List

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        
class BST:
    def __init__(self, val):
        self.root = Node(val)
        
    # O(log(n)) time and O(1) space
    def insert(self, node, x: int):
        if x <= node.val:
            if node.left is None:
                node.left = Node(x)
            else:
                self.insert(node.left, x)
        else:
            if node.right is None:
                node.right = Node(x)
            else:
                self.insert(node.right, x)
    
    # O(n) time and O(n) space
    def inorder(self, node, traversal):
        if node is None: return traversal
        self.inorder(node.left, traversal)
        traversal.append(node.val)
        self.inorder(node.right, traversal)
        return traversal
    
class SummaryRanges:

    def __init__(self):
        self.tree = None
        self.inserted = set()

    # O(log(n)) time
    def addNum(self, value: int) -> None:
        if value in self.inserted: return
        
        if self.tree is None:
            self.tree = BST(value)
        else:
            self.tree.insert(self.tree.root, value)
            
        self.inserted.add(value)
        
    # O(n) time and O(n) space
    def getIntervals(self) -> List[List[int]]:
        intervals = []

        array = self.tree.inorder(self.tree.root, [])
        if len(array) == 0: return [[]]
        
        left = right = -1
        for value in array:
            if left < 0:
                left = right = value
            
            elif right == value - 1:
                right = value
                
            else:
                intervals.append([left, right])
                left = right = value
                
        intervals.append([left, right])
        return intervals


# January 28, 2023

'''

# Kunal Wadhwa

'''