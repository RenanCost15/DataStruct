"""Capítulo 5 — Projeto 10: iterador fail-fast em ArrayBag."""


class ArrayBag:
    DEFAULT_CAPACITY = 10

    def __init__(self, sourceCollection=None):
        self.items = [None] * self.DEFAULT_CAPACITY
        self.size = 0
        self.modCount = 0
        if sourceCollection:
            for item in sourceCollection:
                self.add(item)

    def __len__(self):
        return self.size

    def __iter__(self):
        modCount = self.modCount
        cursor = 0
        while cursor < len(self):
            yield self.items[cursor]
            if modCount != self.modCount:
                raise RuntimeError("a coleção foi alterada durante a iteração")
            cursor += 1

    def clear(self):
        self.size = 0
        self.items = [None] * self.DEFAULT_CAPACITY
        self.modCount += 1

    def add(self, item):
        if len(self) == len(self.items):
            self.items.extend([None] * len(self.items))
        self.items[len(self)] = item
        self.size += 1
        self.modCount += 1

    def remove(self, item):
        if item not in self:
            raise KeyError(item)
        index = 0
        while self.items[index] != item:
            index += 1
        for cursor in range(index, len(self) - 1):
            self.items[cursor] = self.items[cursor + 1]
        self.size -= 1
        self.items[len(self)] = None
        self.modCount += 1


if __name__ == "__main__":
    bag = ArrayBag([1, 2, 3])
    iterator = iter(bag)
    print(next(iterator))
    bag.add(4)
    try:
        print(next(iterator))
    except RuntimeError as error:
        print("Mutação detectada:", error)
