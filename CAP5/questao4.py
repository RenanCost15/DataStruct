"""Capítulo 5 — Projeto 4: ArrayBag.remove com redução do array."""


class ArrayBag:
    DEFAULT_CAPACITY = 10

    def __init__(self, sourceCollection=None):
        self.items = [None] * self.DEFAULT_CAPACITY
        self.size = 0
        if sourceCollection:
            for item in sourceCollection:
                self.add(item)

    def __len__(self):
        return self.size

    def __iter__(self):
        for index in range(len(self)):
            yield self.items[index]

    def add(self, item):
        if len(self) == len(self.items):
            self.items.extend([None] * len(self.items))
        self.items[len(self)] = item
        self.size += 1

    def remove(self, item):
        if item not in self:
            raise KeyError(str(item) + " não está na bag")
        targetIndex = 0
        while self.items[targetIndex] != item:
            targetIndex += 1
        for index in range(targetIndex, len(self) - 1):
            self.items[index] = self.items[index + 1]
        self.size -= 1
        self.items[len(self)] = None

        if (len(self) <= len(self.items) // 4
                and len(self.items) >= self.DEFAULT_CAPACITY * 2):
            newCapacity = max(self.DEFAULT_CAPACITY, len(self.items) // 2)
            newItems = [None] * newCapacity
            for index in range(len(self)):
                newItems[index] = self.items[index]
            self.items = newItems


if __name__ == "__main__":
    bag = ArrayBag(range(30))
    before = len(bag.items)
    for value in range(25):
        bag.remove(value)
    print("Capacidade antes/depois:", before, len(bag.items))
    print("Itens restantes:", list(bag))
