from typing import Optional, Any


class HashMap:
    def __init__(self, capacity: Optional[int] = 10):
        self.__capacity = capacity
        self.__size = 0
        self.__buckets = [[] for _ in range(self.__capacity)]

    @property
    def capacity(self) -> int:
        return self.__capacity

    @property
    def size(self) -> int:
        return self.__size

    def __hash(self, key: Any) -> int:
        return hash(key)

    def __getitem__(self, key: Any):
        index = self.__hash(key) % self.__capacity
        bucket = self.__buckets[index]

        for k, v in bucket:
            if k == key:
                return v

        raise KeyError(f'No item with key \"{key}\" in map.')

    def __setitem__(self, key: Any, value: Any):
        index = self.__hash(key) % self.__capacity
        bucket = self.__buckets[index]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return

        bucket.append((key, value))
        self.__size += 1

    def __delitem__(self, key: Any):
        index = self.__hash(key) % self.__capacity
        bucket = self.__buckets[index]

        for i, (k, _) in enumerate(bucket):
            if k == key:
                del bucket[i]
                self.__size -= 1
                return

        raise KeyError(f'Failed to delete, \"{key}\" not found.')

    def __len__(self):
        return self.__size
