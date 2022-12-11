# Question: https://leetcode.com/problems/number-of-restricted-paths-from-first-to-last-node/
# Medium
# Slightly tricky. Hint: DP
from typing import Optional, List

import math
from heapq import heapify, heappop as hpop, heappush as hpush
class Solution:
    # O((|E| + |V|) * log(V)) Time and O(V + E) Space
    def countRestrictedPaths(self, n: int, edges: List[List[int]]) -> int:
        mod = (10**9) + 7
        graph = [set() for _ in range(n+1)]
        distances = [math.inf] * (n + 1)
        distances[n] = 0
        
        for source, dest, weight in edges:
            graph[source].add((weight, dest))
            graph[dest].add((weight, source))
            

        unexplored = [(0, n)]
        heapify(unexplored)
        explored = set()
        
        # dynamic-programming
        # at every index of ways, where index represents the node-id
        # we will store the number of ways we can reach this node
        # from node-1, with condition node-1's distance from node-n
        # is greater than this node's distance from node-n
        ways = [0] * (n+1)
        ways[n] = 1
        
        # dijkstra's algorithm
        # we are calculating shortest distance of each node
        # from node-n
        # and, along with that we are calculating number of restricted paths
        # from node-1 to node-n in bottom-up fashion
        while len(unexplored) != 0:
            weight, node = hpop(unexplored)
            
            if node in explored: continue
            explored.add(node)
            
            for adj_weight, adj_node in graph[node]:
                if adj_node in explored: continue
                    
                new_weight = adj_weight + weight
                
                # update shortest-distance
                if new_weight < distances[adj_node]:
                    distances[adj_node] = new_weight
                    hpush(unexplored, (new_weight, adj_node))
           
                # update the number of ways/paths
                # we know that we have already explored node
                # so, we can use it's precomputed distance
                if distances[adj_node] > distances[node]:
                    ways[adj_node] += ways[node]
                    
        return ways[1] % mod
                    
'''

# Kunal Wadhwa

'''