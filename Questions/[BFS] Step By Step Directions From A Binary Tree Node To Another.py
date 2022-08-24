# Question: https://leetcode.com/problems/step-by-step-directions-from-a-binary-tree-node-to-another/
# Medium
#
from typing import Optional, List
from collections import defaultdict, deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # Kinda-Brute
    # Memory-Limit Exceeded
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        parents = {}
        def fill_parents(node, parent):
            if node is None: return
            parents[node] = parent
            fill_parents(node.left , node)
            fill_parents(node.right, node)
            
        fill_parents(root, None)
        
        def path_to_node(node, dest, path):
            if node is None:
                return (False, path)
            
            if node.val == dest:
                return (True, path)
            
            left_subtree  = path_to_node(node.left, dest , path+'L')
            right_subtree = path_to_node(node.right, dest, path+'R')
            
            if left_subtree[0]  is True: return (True, left_subtree[1])
            if right_subtree[0] is True: return (True, right_subtree[1])
            return (False, path)
        
        def find_node(node, target):
            if node is None: return None
            if node.val == target: return node
            left_subtree  = find_node(node.left, target)
            right_subtree = find_node(node.right, target)
            if left_subtree is not None : return left_subtree
            if right_subtree is not None: return right_subtree
            return None
        
        start_node = find_node(root, startValue)
        find_down = path_to_node(start_node, destValue, '')
        if find_down[0] is True: return find_down[1]
        
        path = ''
        while start_node is not None:
            parent = parents[start_node]
            start_node = parent
            path += 'U'
            find_down = path_to_node(parent, destValue, path)
            if find_down[0] is True: return find_down[1]
        
        return 
        
    # Time-Limit Exceeded
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:       
        def path_to_node(node, dest, path):
            if node is None:
                return (False, path)
            
            if node.val == dest:
                return (True, path)
            
            left_subtree  = path_to_node(node.left, dest , path+'L')
            right_subtree = path_to_node(node.right, dest, path+'R')
            
            if left_subtree[0]  is True: return (True, left_subtree[1])
            if right_subtree[0] is True: return (True, right_subtree[1])
            return (False, path)

        def lowest_common_ancestor(node):
            if node is None: return node
            if any([node.val == startValue, node.val == destValue]):
                return node
            left_subtree  = lowest_common_ancestor(node.left)
            right_subtree = lowest_common_ancestor(node.right)
            
            if all([left_subtree is not None, right_subtree is not None]):
                return node
            if left_subtree is not None:
                return left_subtree
            else:
                return right_subtree
        
        
        lca = lowest_common_ancestor(root)
        source_path = path_to_node(lca, startValue, '')[1]
        dest_path   = path_to_node(lca, destValue , '')[1]
        
        return 'U'*len(source_path) + dest_path
    
    # Accepted
    # O(V + E) Time and O(V + E) Space
    # V = number of nodes in the tree = n
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        # build graph
        graph = defaultdict(set)
        stack = [root]
        
        while len(stack) != 0:
            node = stack.pop()
            
            if node.left is not None:
                graph[node.val].add((node.left.val, 'L'))
                graph[node.left.val].add((node.val, 'U'))
                stack.append(node.left)
                
            if node.right is not None:
                graph[node.val].add((node.right.val, 'R'))
                graph[node.right.val].add((node.val, 'U'))
                stack.append(node.right)
                
        # Breadth-First-Search
        # From source
        queue = deque()
        queue.append((startValue, ''))
        visited = set()
        
        while len(queue) != 0:
            node, path = queue.pop()
            visited.add(node)
            
            if node == destValue:
                return path
            
            for adjnode, direction in graph[node]:
                if adjnode not in visited:
                    queue.append((adjnode, path+direction))
        
        return ''

'''

# Kunal Wadhwa

'''