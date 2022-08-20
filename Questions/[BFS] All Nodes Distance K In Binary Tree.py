# Question: https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/
# Medium
from typing import Optional, List

from collections import deque
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
class Graph:
    # Create a graph node using a tree node and fill it's connected neighbors using tree node's children and it's parent
    def __init__(self, node=None, parent=None):
        self.node      = node
        self.neighbors = list()
        self.fill_neighbors(parent)
        
    # Recursively fill neighbors, thereby forming an entire graph from one tree node
    def fill_neighbors(self, parent):
        if parent:
            self.neighbors.append(parent)
            
        if self.node.left:
            self.neighbors.append(Graph(self.node.left, self))
            
        if self.node.right:
            self.neighbors.append(Graph(self.node.right, self))
            
            
    # Given a graph node and a target tree node finds and returns the graph node which corresonds to the given tree ndoe
    def get_target_node(self, graph, target):
        q       = deque([graph])
        visited = dict()
        
        while len(q):
            gnode = q.popleft()
            if gnode in visited: continue
                
            if gnode.node == target:
                return gnode
            
            for neighbor in gnode.neighbors:
                if neighbor.node == target:
                    return neighbor
                q.append(neighbor)
                
            visited[gnode] = True
        
        return None
    
    
    # Given a graph node, finds all the node's value which are distance away from this node
    def get_distance_away_nodes(self, start, distance):
        result  = list()
        visited = dict()
        def helper(gnode, distance):
            if gnode in visited:
                return 
            
            visited[gnode] = True
            
            if distance == 0:
                result.append(gnode.node.val)
                return
            
            for neighbor in gnode.neighbors:
                helper(neighbor, distance-1)
        
        helper(start, distance)
        return result

class Solution:
    '''
    O(v + e) Time and O(v) Space: where v is the number of tree nodes, e is the number of children + parent of the tree node
    '''
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        if k == 0: return [target.val]
        if not target or not root: return None
        
        # create a graph from the tree
        graph = Graph(root)
        
        # find the corresponding graph node for target tree node
        target_node = graph.get_target_node(graph, target)
        
        # start DFS from this node and find all the nodes which are distance away from this node
        result = target_node.get_distance_away_nodes(target_node, k)
        
        return result

    '''
    O(n*d) Time and O(n) Space: where n is the number of nodes and d is the distance
    '''
    def distance_k(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        if not target or not root: return None
        
        hashmap = dict()
        result  = list()
        
        # - Fill the hasmap with key, value pair as node, node's parent for all the nodes that were traversed in the path from root to target
        # - Once, the target is found. It will find the nodes that are k distance away from the target node down the tree
        # Doesn't return anything
        
        def helper(node: TreeNode, parent=None, distance=float('inf'), found=False) -> None:
            if node is None: return
            
            # node, parent pair
            hashmap[node] = parent

            # We'll mark target as found, and start looking for k distance away nodes
            # for that, we'll change distance from infinity to 0
            if node == target:
                found    = True
                distance = 0
            
            if distance == k:
                result.append(node.val)
                return
            
            # At every call, the distance of next node from target node will increase by one
            helper(node.left , node, distance + 1 if found else distance, found)
            helper(node.right, node, distance + 1 if found else distance, found)
            
            return
        
        # given a node and a distance, and has a reference to a list
        # appends values of all the nodes that are distance away from the given node
        def get_nodes_distance_away(node, distance):
            if node is None or distance < 0: return None
            
            if distance == 0: result.append(node.val)
                
            get_nodes_distance_away(node.left, distance-1)
            get_nodes_distance_away(node.right, distance-1)
            
            return
        
        
        # calling the helper to fill the hashmap of key, value that is = node, parent
        # and to fill the resultant list with all the nodes values which are distance away down from the target node
        helper(root)
        
        
        # now, we need to find the nodes that are distance away from target in the up side
        # we start by moving one node up at a time and keeping track of the distance we move away from the target
        # two cases can happen
        #   - the node we are currently at is the distance = k away, in which case we append it's value to the result
        #   - there may be nodes present in the other half of this node that are distance away from the target, in which case we need to explore  it's other half. If we came from right, we explore the left and vice versa
        
        # checking if target is not root, coz if it's root we can't check up and we stop
        if hashmap[target]:
            distance = k
            parent   = target
            
            # while we can still go up
            while distance > 0:
                child   = parent
                parent  = hashmap[child]
                
                # if parent is root
                if not hashmap[parent]:
                    # we explore the other half
                    target_node = parent.left if parent.left != child else parent.right
                    # parent is distance away, we don't need or we can't explore more
                    if distance - 1 == 0:
                        result.append(parent.val)
                        break
                        
                    # otherwise, we can explore
                    get_nodes_distance_away(target_node, distance-2)
                    break
                    
                # check the half we haven't explored
                target_node = parent.left if parent.left != child else parent.right
                distance -= 1
                # if distance equals 0, we can't explore anymore, we stop
                if distance == 0:
                    result.append(parent.val)
                    break
                    
                # keep exploring
                get_nodes_distance_away(target_node, distance-1)
                
        return result


# Kunal Wadhwa
