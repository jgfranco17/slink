from typing import Any

from .nodes import BinaryTreeNode


class BinaryTree:
    """A Tree node has data variable and pointers to nodes to its left and
    right."""

    def __init__(self, root: BinaryTreeNode) -> None:
        self.root = root
        self.left: BinaryTree | None = None
        self.right: BinaryTree | None = None

    @property
    def depth(self):
        return self.__depth_of_tree(self.root)

    @property
    def is_full_binary_tree(self):
        return self.__check_full_tree(self.root)

    def __display(self, tree) -> None:  # In Order traversal of the tree
        """Display the tree."""
        if tree:
            self.__display(tree.left)
            print(tree.data)
            self.__display(tree.right)

    def display(self) -> None:
        self.__display(self.root)

    def __depth_of_tree(self, tree) -> int:
        """Recursive function that returns the depth of a binary tree."""
        return (
            1 + max(self.__depth_of_tree(tree.left), self.__depth_of_tree(tree.right))
            if tree
            else 0
        )

    def __check_full_tree(self, tree) -> bool:
        """Returns True if this is a full binary tree."""
        if not tree:
            return True
        if tree.left and tree.right:
            return self.is_full_binary_tree(tree.left) and self.is_full_binary_tree(
                tree.right
            )
        else:
            return not tree.left and not tree.right
