from typing import Any
from .nodes import TreeNode


class BinaryTree:
    """
    A BinaryTree has data variable and pointers to Nodes to its left and right.
    """
    def __init__(self, root: TreeNode) -> None:
        self.root = root

    def __bool__(self):
        return self.data is not None

    @property
    def depth(self):
        return self.__get_depth(self.root)
        
    def __get_depth(self, node):
        """
        Recursive function that returns the depth of a binary tree.
        """
        return 1 + max(self.depth(node.left), self.depth(node.right)) if node else 0
