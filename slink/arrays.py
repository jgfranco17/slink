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
        if size < self.__size:
            self.__data = self.__data[:size]
        else:
            self.__data += [None] * (size - self.__size)
        self.__size = size

    def insert(self, index, value):
        if not 0 <= index <= self.__size:
            raise IndexError('Index out of range')
        self.resize(self.__size + 1)
        for i in range(self.__size - 1, index, -1):
            self.__data[i] = self.__data[i-1]
        self.__data[index] = value

    def remove(self, value):
        for i in range(self.__size):
            if self.__data[i] == value:
                self.__data[i] = None
                for j in range(i+1, self.__size):
                    self.__data[j-1] = self.__data[j]
                self.resize(self.__size - 1)
                return

        raise ValueError(f'{value} not found')
