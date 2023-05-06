from typing import Any


class BinaryTree:
    """
    A BinaryTree has data variable and pointers to Nodes to its left and right.
    """
    def __init__(self, data: Any) -> None:
        self.data = data
        self.left: BinaryTree | None = None
        self.right: BinaryTree | None = None
        
    def depth(self):
        """
        Recursive function that returns the depth of a binary tree.
        """
        return 1 + max(self.depth(self.left), self.depth(self.right)) if self else 0