from typing import Any


class ListNode:
    def __init__(self, data: Any):
        self.data = data
        self.next = None

    def __repr__(self) -> str:
        return f'<ListNode at {hex(id(self))}, data={self.data}>'

    @property
    def address(self):
        return hex(id(self))


class TreeNode:
    def __init__(self, data: Any) -> None:
        self.data = data
        self.left: TreeNode | None = None
        self.right: TreeNode | None = None

    def __bool__(self):
        return self.data is not None