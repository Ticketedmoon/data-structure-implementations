from collections import OrderedDict

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()
        self.cache_size = 0

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key, last = True)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            if self.cache_size == self.capacity:
                self.cache.popitem(last = False)
            else:
                self.cache_size += 1

        self.cache[key] = value
        self.cache.move_to_end(key, last = True)
