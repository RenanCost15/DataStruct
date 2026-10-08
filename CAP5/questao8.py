"""Capítulo 5 — Projeto 8: ArraySortedBag em ordem crescente."""


class ArraySortedBag:
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

    def __contains__(self, item):
        """Busca binária: O(log n)."""
        left = 0
        right = len(self) - 1
        while left <= right:
            midpoint = (left + right) // 2
            if self.items[midpoint] == item:
                return True
            if item < self.items[midpoint]:
                right = midpoint - 1
            else:
                left = midpoint + 1
        return False

    def add(self, item):
        """Insere na posição correta e mantém a ordem crescente."""
        if len(self) == len(self.items):
            self.items.extend([None] * len(self.items))
        index = 0
        while index < len(self) and self.items[index] <= item:
            index += 1
        for cursor in range(len(self), index, -1):
            self.items[cursor] = self.items[cursor - 1]
        self.items[index] = item
        self.size += 1


if __name__ == "__main__":
    bag = ArraySortedBag([5, 1, 4, 2, 3, 3])
    print("Ordem crescente:", list(bag))
    print("3 presente:", 3 in bag)
    print("8 presente:", 8 in bag)
