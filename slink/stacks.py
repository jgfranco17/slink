from typing import Any
from .structexceptions import StackUnderflowError, StackOverflowError


class Stack:
    """
    A stack is an abstract data type that serves as a collection of elements with 
    two principal operations: 'push' and 'pop'. Pushing adds an element to the top
    of the stack, and popping removes an element from the top of a stack. The order
    in which elements come off of a stack are Last In First Out (LIFO).
    """

    def __init__(self, limit: int = 10):
        self.__stack: list[Any] = []
        self.__limit = limit

    def __bool__(self) -> bool:
        return bool(self.__stack)

    def __len__(self) -> int:
        return len(self.__stack)

    def __repr__(self) -> str:
        return f'<Stack at {hex(id(self))}, limit={self.__limit}'

    def __str__(self) -> str:
        items = " ".join(str(self.__stack))
        return f'[{items}]'

    @property
    def is_empty(self) -> bool:
        """
        Check if a stack is empty.
        """
        return not bool(self.__stack)

    @property
    def is_full(self) -> bool:
        """
        Check if the stack is full.
        """
        return self.size() == self.__limit

    @property
    def size(self) -> int:
        """
        Return the size of the stack.
        """
        return len(self.__stack)

    @property
    def limit(self) -> int:
        return self.__limit

    def push(self, data: Any) -> None:
        """
        Push an element to the top of the stack.
        """
        if len(self.__stack) >= self.__limit:
            raise StackOverflowError(f'Stack has limit of {self.__limit}.')

        self.__stack.append(data)

    def pop(self) -> Any:
        """
        Pop an element off of the top of the stack.
        """
        if not self.__stack:
            raise StackUnderflowError(f'Cannot pop from empty stack.')

        return self.__stack.pop()

    def peek(self) -> Any:
        """
        Peek at the top-most element of the stack.
        """
        if not self.__stack:
            raise StackUnderflowError

        return self.__stack[-1]
