from typing import Any
from .nodes import GraphNode


class Graph:
    """
    A graph is a data structure that consists of a collection of vertices (or nodes)
    connected by edges. Graphs can be directed, meaning the edges have a specific
    direction, or undirected, meaning the edges have no direction. Graphs are often
    used to represent networks, such as social networks or transportation systems,
    or to solve problems in algorithmic graph theory.
    """
    def __init__(self):
        """
        Initializes an empty graph with no nodes.
        """
        self.nodes = set()

    def add_node(self, value: Any):
        """
        Adds a node with the given value to the graph.
        """
        node = GraphNode(value)
        self.nodes.add(node)

    def add_edge(self, start: GraphNode, end: GraphNode):
        """
        Adds a directed edge from the start node to the end node in the graph.
        """
        start.add_neighbor(end)

    def remove_node(self, node: GraphNode):
        """
        Removes the given node and all its incident edges from the graph.
        """
        if node in self.nodes:
            self.nodes.remove(node)
            for n in self.nodes:
                if node in n.neighbors:
                    n.neighbors.remove(node)

    def remove_edge(self, start, end):
        """
        Removes a directed edge from the start node to the end node in the graph.
        """
        if start in self.nodes and end in self.nodes:
            if end in start.neighbors:
                start.neighbors.remove(end)

    def depth_first_search(self, start):
        """
        Performs a depth-first search traversal of the graph, starting at the given node.
        """
        visited = set()
        self._dfs_helper(start, visited)

    def _dfs_helper(self, node, visited):
        """
        A helper method for depth_first_search, recursively traversing the graph.
        """
        visited.add(node)
        print(node.data)
        for neighbor in node.neighbors:
            if neighbor not in visited:
                self._dfs_helper(neighbor, visited)

    def breadth_first_search(self, start):
        """
        Performs a breadth-first search traversal of the graph, starting at the given node.
        """
        visited = set()
        queue = [start]
        visited.add(start)
        while queue:
            node = queue.pop(0)
            print(node.data)
            for neighbor in node.neighbors:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)