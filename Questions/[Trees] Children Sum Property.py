# Question: https://www.codingninjas.com/codestudio/problems/childrensumproperty_790723
# Medium
from typing import Optional, List

from os import *
from sys import *
from collections import *
from math import *

'''
 
    Following is the Binary Tree node structure
    
    class BinaryTreeNode:
        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None

'''
        
# O(n) Time and O(h) Space 
def changeTree(root): 
    # Write your code here.
    def satisfy(node, passed_down):
        if node is None:
            return
        
        node.data += passed_down
        
        left  = 0 if node.left is None else node.left.data
        right = 0 if node.right is None else node.right.data
        
        if left + right < node.data:
            pass_down = node.data - (left + right)
        else:
            pass_down = 0
            
        if node.left is not None and node.right is not None:
            pass_left = pass_down // 2
            pass_right = pass_down - pass_left
            satisfy(node.left, pass_left)
            satisfy(node.right, pass_right)
            
        elif node.left is not None:
            satisfy(node.left, pass_down)
            
        elif node.right is not None:
            satisfy(node.right, pass_down)
            
        left  = 0 if node.left is None else node.left.data
        right = 0 if node.right is None else node.right.data
        
        if left + right != 0:
            node.data = left + right
        
    satisfy(root, 0)
    
     	
'''

# Kunal Wadhwa

'''