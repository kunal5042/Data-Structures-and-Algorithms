# Question: https://leetcode.com/problems/is-graph-bipartite/
# Medium

from typing import List

class Solution:
    # O(v + e) time and O(v) space
    def isBipartite(self, graph: List[List[int]]) -> bool:
        # Initialize arrays to keep track of colors and visited nodes
        # Colors assigned to nodes: 0 (not assigned), 1 or -1
        color = [0 for _ in range(len(graph))]  
        
        # Mark nodes as visited during traversal
        visited = [False for _ in range(len(graph))]  
        
        def allot_color(source, to_allot):
            # DFS traversal to assign colors to nodes
            visited[source] = True
            color[source] = to_allot
            
            for neighbor in graph[source]:
                if visited[neighbor] is True:
                    # If the neighbor node has been visited, check if the colors conflict
                    # Conflict in coloring, graph is not bipartite
                    if color[neighbor] == to_allot:
                        return False  
                    
                    # Skip to next neighbor if already visited
                    continue  
                    
                # Recursively assign colors to neighbor nodes
                if allot_color(neighbor, to_allot * -1) is False:
                    # Propagate the False result if a conflict is encountered
                    return False  
                
            # All nodes assigned colors without conflicts
            return True  
        
        alloted_color = 1  # Start with color 1
        for node in range(len(graph)):
            if visited[node] is False:
                # Start DFS traversal from unvisited nodes and assign colors to their components
                if allot_color(node, alloted_color) is False:
                    # Conflict in coloring, graph is not bipartite
                    return False  
                
                # Alternate color for the next component
                alloted_color *= -1  
        
         # No conflicts encountered, graph is bipartite
        return True 



# May 19, 2023

'''

# Kunal Wadhwa

'''