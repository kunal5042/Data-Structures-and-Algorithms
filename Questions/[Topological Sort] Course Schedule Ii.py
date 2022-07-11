# Question: https://leetcode.com/problems/course-schedule-ii/

from typing import Optional, List

from typing import List
class Node:
    def __init__(self, value):
        self.value = value
        self.children = []
        
    def add_child(self, child):
        self.children.append(child)

class Solution:
    def findOrder(self, num_courses: int, prerequisites: List[List[int]]) -> List[int]:
        visited, callstack = set(), set()
        
        def create_nodes() -> dict:
            """Creates a node for each course and returns their reference in a hashmap"""
            hashmap = {}
            for course in range(num_courses):
                hashmap[course] = Node(course)
            return hashmap
        
        def add_prerequisites(graph, preq) -> None:
            """Adds prerequisites/children of the courses/nodes"""
            for idx in range(len(preq)):
                course, prereq = preq[idx]
                graph[course].add_child(graph[prereq])
            return
        
        def is_prereq_satisfied(node, ordered_courses) -> bool:
            """Takes a node representing a course, checks if prerequisites of this course can
            be satisfied
            """
            if node in callstack: return False
            if node in visited  : return True

            callstack.add(node)
            visited.add(node)
            
            for child in node.children:
                if is_prereq_satisfied(child, ordered_courses) is False:
                    return False
            
            callstack.remove(node)
            ordered_courses.append(node.value)
            return True
        
        
        def get_ordered_courses(graph) -> List[int]:
            """Takes a graph where nodes represent the courses and their children
            represents their prerequisites. Returns a list of ordering of the courses in 
            which all the courses can be successfully completed.
            If no such ordering exists, returns an empty list
            """
            ordered_courses = []
            for course in range(num_courses):
                if is_prereq_satisfied(graph[course], ordered_courses) is False:
                    return []
                
            return ordered_courses
        
        graph = create_nodes()
        add_prerequisites(graph, prerequisites)
        return get_ordered_courses(graph)
'''

# Kunal Wadhwa

'''