from typing import Any
from .nodes import ListNode


class LinkedList:
    def __init__(self):
        """
        Create and initialize LinkedList class instance.
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
        return " -> ".join([str(item) for item in self])

    def __getitem__(self, index: int) -> Any:
        """
        Indexing Support. Used to get a node at particular position.
        """
        if not 0 <= index < len(self):
            raise IndexError("List index out of range.")

        for i, node in enumerate(self):
            if i == index:
                return node

        return None

    def __setitem__(self, index: int, data: Any) -> None:
        """
        Set the value at a specific index.
        """
        if not 0 <= index < len(self):
            raise IndexError("List index out of range.")

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
            raise IndexError("List index out of range.")

        new_node = ListNode(data)
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
            next_node = current.next
            current.next = prev
            prev, current = current, next_node

        self.head = prev


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        """
        For iterators to access and iterate through data inside doubly-linked list.
        """
        node = self.head
        while node:
            yield node.data
            node = node.next

    def __str__(self):
        return "->".join([str(item) for item in self])

    def __len__(self):
        return sum(1 for _ in self)

    def insert_at_head(self, data):
        self.insert_at_nth(0, data)

    def insert_at_tail(self, data):
        self.insert_at_nth(len(self), data)

    def insert_at_nth(self, index: int, data):
        """
        Insert data at specified index.
        """
        length = len(self)

        if not 0 <= index <= length:
            raise IndexError("List index out of range")

        new_node = ListNode(data)
        if self.head is None:
            self.head = self.tail = new_node
        elif index == 0:
            self.head.previous = new_node
            new_node.next = self.head
            self.head = new_node
        elif index == length:
            self.tail.next = new_node
            new_node.previous = self.tail
            self.tail = new_node
        else:
            temp = self.head
            for _ in range(0, index):
                temp = temp.next
            temp.previous.next = new_node
            new_node.previous = temp.previous
            new_node.next = temp
            temp.previous = new_node

    def delete_head(self):
        return self.delete_at_nth(0)

    def delete_tail(self):
        return self.delete_at_nth(len(self) - 1)

    def delete_at_nth(self, index: int):
        """
        Delete data at specified index.
        """
        length = len(self)

        if not 0 <= index <= length - 1:
            raise IndexError("list index out of range")
        delete_node = self.head  # default first node
        if length == 1:
            self.head = self.tail = None
        elif index == 0:
            self.head = self.head.next
            self.head.previous = None
        elif index == length - 1:
            delete_node = self.tail
            self.tail = self.tail.previous
            self.tail.next = None
        else:
            temp = self.head
            for _ in range(0, index):
                temp = temp.next
            delete_node = temp
            temp.next.previous = temp.previous
            temp.previous.next = temp.next
        return delete_node.data

    def delete(self, data) -> str:
        current = self.head

        while current.data != data:  # Find the position to delete
            if current.next:
                current = current.next
            else:  # We have reached the end an no value matches
                raise ValueError("No data matching given value")

        if current == self.head:
            self.delete_head()

        elif current == self.tail:
            self.delete_tail()

        else:  # Before: 1 <--> 2(current) <--> 3
            current.previous.next = current.next  # 1 --> 3
            current.next.previous = current.previous  # 1 <--> 3
        return data

    def is_empty(self):
        """
        Check if list is empty.
        """
        return len(self) == 0
