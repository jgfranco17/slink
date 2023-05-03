from typing import Any


class Node:
    def __init__(self, data: Any):
        """
        Create and initialize Node class instance.
        """
        self.data = data
        self.next = None

    def __repr__(self) -> str:
        """
        Get the string representation of this node.
        """
        return f"Node({self.data})"

    @property
    def address(self):
        return hex(id(self))