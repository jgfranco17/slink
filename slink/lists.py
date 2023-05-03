from typing import Any
from .nodes import Node


class LinkedList:
    def __init__(self):
        """
        Create and initialize LinkedList class instance.
        >>> linked_list = LinkedList()
        """
        self.head = None

    def __iter__(self) -> Any:
        """
        For iterators to access and iterate through data inside linked list.
        """
        node = self.head
        while node:
            yield node.data
            node = node.next

    def __len__(self) -> int:
        """
        Return length of linked list i.e. number of nodes.
        """
        return sum(1 for _ in self)

    def __repr__(self) -> str:
        """
        String representation/visualization of a Linked Lists.
        """
        return " -> ".join([f'[{item}]' for item in self])

    def __getitem__(self, index: int) -> Any:
        """
        Indexing Support. Used to get a node at particular position.
        """
        if not 0 <= index < len(self):
            raise ValueError("list index out of range.")
        for i, node in enumerate(self):
            if i == index:
                return node
        return None

    def __setitem__(self, index: int, data: Any) -> None:
        """
        Set the value at a specific index.
        """
        if not 0 <= index < len(self):
            raise ValueError("List index out of range.")
        current = self.head
        for _ in range(index):
            current = current.next
        current.data = data

    def insert_tail(self, data: Any) -> None:
        """
        Insert data to the end of linked list.
        """
        self.insert_nth(len(self), data)

    def insert_head(self, data: Any) -> None:
        """
        Insert data to the beginning of linked list.
        """
        self.insert_nth(0, data)

    def insert_nth(self, index: int, data: Any) -> None:
        """
        Insert data at given index.
        """
        if not 0 <= index <= len(self):
            raise IndexError("list index out of range")
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        elif index == 0:
            new_node.next = self.head  # link new_node to head
            self.head = new_node
        else:
            temp = self.head
            for _ in range(index - 1):
                temp = temp.next
            new_node.next = temp.next
            temp.next = new_node

    def print_list(self) -> None:  # print every node data
        """
        This method prints every node data.
        """
        print(self)

    def delete_head(self) -> Any:
        """
        Delete the first node and return the node's data.
        """
        return self.delete_nth(0)

    def delete_tail(self) -> Any:  # delete from tail
        """
        Delete the tail end node and return the node's data.
        """
        return self.delete_nth(len(self) - 1)

    def delete_nth(self, index: int = 0) -> Any:
        """
        Delete node at given index and return the node's data.
        """
        if not 0 <= index <= len(self) - 1:  # test if index is valid
            raise IndexError("List index out of range.")
        delete_node = self.head  # default first node
        if index == 0:
            self.head = self.head.next
        else:
            temp = self.head
            for _ in range(index - 1):
                temp = temp.next
            delete_node = temp.next
            temp.next = temp.next.next
        return delete_node.data

    def is_empty(self) -> bool:
        """
        Check if linked list is empty.
        """
        return self.head is None

    def reverse(self) -> None:
        """
        This reverses the linked list order.
        """
        prev = None
        current = self.head

        while current:
            # Store the current node's next node.
            next_node = current.next
            # Make the current node's next point backwards
            current.next = prev
            # Make the previous node be the current node
            prev = current
            # Make the current node the next node (to progress iteration)
            current = next_node
        # Return prev in order to put the head at the end
        self.head = prev
