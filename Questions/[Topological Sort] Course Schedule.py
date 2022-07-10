# Question: https://leetcode.com/problems/course-schedule/

from typing import Optional, List

class Node:
    def __init__(self, node):
        self._node = node
        self.children= []
        
    def add_children(self, child):
        self.children.append(child)

class Solution:
    def canFinish(self, num_courses: int, prerequisites: List[List[int]]) -> bool:
        graph, visited, callstack = {}, set(), set()
        
        def get_nodes():
            """Populates the graph hashmap with node objects for each course"""
            for node in range(num_courses):
                graph[node] = Node(node)
            return graph
        
        def add_prerequisites():
            """Adds the dependices for each course"""
            for idx in range(len(prerequisites)):
                node, prereq = prerequisites[idx]
                graph[node].add_children(graph[prereq])
                
        def is_prereq_satisfied(node):
            """Checks if all the dependencies for the current course can be satisfied"""
            if node in callstack:
                return False

            if node in visited:
                return True
            
            callstack.add(node)
            visited.add(node)
            
            for child in node.children:
                if is_prereq_satisfied(child) is False:
                    return False
                
            callstack.remove(node)
            return True
                
        get_nodes()
        add_prerequisites()
        
        for node in range(num_courses):
            if is_prereq_satisfied(graph[node]) is False:
                return False
        
        print(get_nodes.__doc__)
        print(add_prerequisites.__doc__)
        print(is_prereq_satisfied.__doc__)
        return True
        
        
        
'''

# Kunal Wadhwa

'''