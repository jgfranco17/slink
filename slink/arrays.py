from typing import Any


class Array:
    def __init__(self, size: int):
        self.__size = size
        self.__data = [None] * size

    def __len__(self):
        return self.__size

    def __getitem__(self, index: int):
        if not 0 <= index < self.__size:
            raise IndexError("Index out of range")

        return self.__data[index]

    def __setitem__(self, index:int, value: Any):
        if not 0 <= index < self.__size:
            raise IndexError("Index out of range")

        self.__data[index] = value

    def __iter__(self):
        return iter(self.__data)

    def __repr__(self):
        return f'<Array at {hex(id(self))}, size={self.__size}'

    def __str__(self) -> str:
        items = " ".join(list(map(str, self.__data)))
        return f'[{items}]'

    def resize(self, size: int):
        if not isinstance(size, int):
            raise TypeError(f'Expected input of type int but got {type(size)}')

        if size < self.__size:
            self.__data = self.__data[:size]
        else:
            self.__data += [None] * (size - self.__size)
        self.__size = size

    def insert(self, index: int, value: Any):
        if not isinstance(index, int):
            raise TypeError(f'Expected input of type int but got {type(index)}')

        if not 0 <= index <= self.__size:
            raise IndexError("Index out of range")

        self.resize(self.__size + 1)
        for i in range(self.__size - 1, index, -1):
            self.__data[i] = self.__data[i-1]
        self.__data[index] = value

    def remove(self, value: Any):
        for i in range(self.__size):
            if self.__data[i] == value:
                self.__data[i] = None
                for j in range(i+1, self.__size):
                    self.__data[j-1] = self.__data[j]
                self.resize(self.__size - 1)
                return

        raise ValueError(f'{value} not found')

    def __partition(self, low: int, high: int) -> int:
        pivot = self[high]
        i = low - 1
        for j in range(low, high):
            if self[j] <= pivot:
                i += 1
                self[i], self[j] = self[j], self[i]
        self[i + 1], self[high] = self[high], self[i + 1]
        return i + 1

    def __quicksort(self, low: int, high: int) -> None:
        if low < high:
            pi = self.__partition(low, high)
            self.__quicksort(low, pi - 1)
            self.__quicksort(pi + 1, high)

    def sort(self):
        self.__quicksort(0, len(self) - 1)
