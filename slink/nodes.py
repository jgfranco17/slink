from typing import Any


class Node:
    """Base class for node objects."""

    def __init__(self, data: Any):
        self.data = data

    def __bool__(self):
        return self.data is not None

    @property
    def address(self):
        return hex(id(self))


class SinglyLinkedNode(Node):
    def __init__(self, data: Any):
        super().__init__(data)
        self.next: SinglyLinkedNode | None = None

    def __repr__(self) -> str:
        return f"<SinglyLinkedNode at {self.address}, data={self.data}, type={type(self.data)}>"


class DoublyLinkedNode(Node):
    def __init__(self, data: Any):
        super().__init__(data)
        self.next: DoublyLinkedNode | None = None
        self.previous: DoublyLinkedNode | None = None

    def __repr__(self) -> str:
        return f"<DoublyLinkedNode at {self.address}, data={self.data}, type={type(self.data)}>"


class BinaryTreeNode(Node):
    def __init__(self, data: Any) -> None:
        super().__init__(data)
        self.left: BinaryTreeNode | None = None
        self.right: BinaryTreeNode | None = None


class GraphNode:
    def __init__(self, data: Any) -> None:
        super().__init__(data)
        self.neighbors = []

    def __repr__(self) -> str:
        return (
            f"<GraphNode at {self.address}, data={self.data}, type={type(self.data)}>"
        )

    def add_neighbor(self, neighbor):
        """Adds a neighboring node to the node's list of neighbors."""
        self.neighbors.append(neighbor)
