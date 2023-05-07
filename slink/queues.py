from typing import Any


class Queue:
    """
    A queue data structure implemented using a Python list.
    """

    def __init__(self):
        self.items = []

    @property
    def size(self):
        """
        Return the number of items in the queue.
        """
        return len(self.items)

    @property
    def is_empty(self):
        """
        Check if the queue is empty.
        """
        return len(self.items) == 0

    def enqueue(self, item: Any):
        """
        Add an item to the back of the queue.
        """
        self.items.append(item)

    def dequeue(self):
        """
        Remove and return the front item of the queue.
        """
        if self.is_empty():
            raise IndexError("Queue is empty")
        else:
            return self.items.pop(0)
