"""Capítulo 6 — Projeto 1: __eq__ linear em ArraySortedBag."""


class ArraySortedBag:
    def __init__(self, sourceCollection=None):
        self.items = [None] * 10
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
        position = 0
        while position < len(self) and self.items[position] <= item:
            position += 1
        for index in range(len(self), position, -1):
            self.items[index] = self.items[index - 1]
        self.items[position] = item
        self.size += 1

    def __eq__(self, other):
        """Compara pares já ordenados; tempo O(n)."""
        if self is other:
            return True
        if type(self) is not type(other) or len(self) != len(other):
            return False
        otherIterator = iter(other)
        for item in self:
            if item != next(otherIterator):
                return False
        return True


if __name__ == "__main__":
    first = ArraySortedBag([3, 1, 2, 2])
    second = ArraySortedBag([2, 3, 2, 1])
    third = ArraySortedBag([1, 2, 3, 3])
    print("Mesmos itens (esperado True):", first == second)
    print("Itens diferentes (esperado False):", first == third)
