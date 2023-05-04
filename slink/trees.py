from typing import Any


class TreeNode:
    """
    A TreeNode has data variable and pointers to Nodes to its left and right.
    """
    def __init__(self, data: Any) -> None:
        self.data = data
        self.left: TreeNode | None = None
        self.right: TreeNode | None = None
        
    def depth(self):
        """
        Recursive function that returns the depth of a binary tree.
        """
        return 1 + max(self.depth(self.left), self.depth(self.right)) if self else 0