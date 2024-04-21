# Question: https://leetcode.com/problems/find-if-path-exists-in-graph/description/
# Easy

from copy import copy
from collections import deque, defaultdict
from typing import List

class NodeNotFound(Exception):
    """Exception raised when a node is not found in the graph."""

    def __init__(self, node_id: int):
        self.message = f"Node with ID {node_id} doesn't exist in the active graph."
        super().__init__(self.message)


class Node:
    """Represents a node in the graph."""

    def __init__(self, node_id: int):
        """Initialize a Node object.

        Args:
            node_id (int): The ID of the node.
        """
        self.node_id = node_id
        self._adjacents = set()

    def add_edge(self, node: "Node"):
        """Add an edge to another node.

        Args:
            node (Node): The node to connect to.
        """
        self._adjacents.add(node)

    def get_adjacents(self):
        """Get the adjacent nodes."""
        return self._adjacents.copy()

    def __lt__(self, other: "Node"):
        """Comparison method for sorting nodes based on their IDs."""
        return self.node_id < other.node_id


class Graph:
    """Represents a graph."""

    def __init__(self):
        """Initialize a Graph object."""
        self.nodes = defaultdict(lambda: Node(-1))

    def get_node(self, node_id: int) -> Node:
        """Get a node by its ID.

        Args:
            node_id (int): The ID of the node to retrieve.

        Returns:
            Node: The node object.
        """
        return self.nodes[node_id]

    def add_node(self, node_id: int):
        """Add a node to the graph.

        Args:
            node_id (int): The ID of the node to add.
        """
        self.node_exists(node_id)
        self.nodes[node_id] = Node(node_id)

    def connect_nodes(self, src: int, dst: int, bidirect=False) -> bool:
        """Connect two nodes in the graph.

        Args:
            src (int): The ID of the source node.
            dst (int): The ID of the destination node.
            bidirect (bool, optional): Whether to add a bidirectional edge. Defaults to False.

        Returns:
            bool: True if the nodes were connected successfully, False otherwise.
        """
        self.nodes_exist([src, dst])
        self.nodes[src].add_edge(self.nodes[dst])
        if bidirect is True:
            self.nodes[dst].add_edge(self.nodes[src])

    def nodes_exist(self, node_ids: List[int]) -> bool:
        """Check if nodes with the given IDs exist in the graph.

        Args:
            node_ids (List[int]): The IDs of the nodes to check.

        Returns:
            bool: True if all nodes exist, False otherwise.
        """
        for node_id in node_ids:
            if not self.node_exists(node_id):
                return False
        return True

    def node_exists(self, node_id: int) -> bool:
        """Check if a node with the given ID exists in the graph.

        Args:
            node_id (int): The ID of the node to check.

        Returns:
            bool: True if the node exists, False otherwise.
        """
        if node_id not in self.nodes:
            return False
        return True

    def path_exists(self, src: int, dst: int) -> bool:
        """Check if a path exists between two nodes in the graph.

        Args:
            src (int): The ID of the source node.
            dst (int): The ID of the destination node.

        Returns:
            bool: True if a path exists, False otherwise.
        
        Raises:
            NodeNotFound: If the source node does not exist in the graph.
        """
        self.nodes_exist([src, dst])
        visited = set()

        if not self.node_exists(src):
            raise NodeNotFound(src)

        queue = deque([self.get_node(src)])
        while len(queue) != 0:
            node = queue.popleft()
            visited.add(node)

            if node.node_id == dst:
                return True

            for adjacent in node.get_adjacents():
                if adjacent not in visited:
                    queue.append(adjacent)
        
        return False


class Solution:
    """Solution class for the problem."""

    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        """Check if there is a valid path between two nodes in the graph.

        Args:
            n (int): The number of nodes in the graph.
            edges (List[List[int]]): The list of edges represented as pairs of node IDs.
            source (int): The ID of the source node.
            destination (int): The ID of the destination node.

        Returns:
            bool: True if a valid path exists, False otherwise.
        """
        graph = Graph()

        for node_id in range(n):
            graph.add_node(node_id)

        for u, v in edges:
            graph.connect_nodes(u, v, True)

        return graph.path_exists(source, destination)



# April 21, 2024

'''

# Kunal Wadhwa

'''