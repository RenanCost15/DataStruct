"""Capítulo 6 — Projeto 3: AbstractCollection e AbstractBag completas."""


class AbstractCollection:
    """Comportamento comum a todas as coleções do framework."""

    def __init__(self, sourceCollection=None):
        self.size = 0
        if sourceCollection:
            for item in sourceCollection:
                self.add(item)

    def isEmpty(self):
        return len(self) == 0

    def __len__(self):
        return self.size

    def __str__(self):
        return "[" + ", ".join(map(str, self)) + "]"

    def __eq__(self, other):
        if self is other:
            return True
        if type(self) is not type(other) or len(self) != len(other):
            return False
        otherIterator = iter(other)
        for item in self:
            if item != next(otherIterator):
                return False
        return True

    def count(self, item):
        return sum(1 for current in self if current == item)

    def __add__(self, other):
        result = type(self)(self)
        for item in other:
            result.add(item)
        return result

    def clone(self):
        return type(self)(self)


class AbstractBag(AbstractCollection):
    """Especializa representação textual e igualdade de bags não ordenadas."""

    def __str__(self):
        return "{" + ", ".join(map(str, self)) + "}"

    def __eq__(self, other):
        if self is other:
            return True
        if type(self) is not type(other) or len(self) != len(other):
            return False
        return all(self.count(item) == other.count(item) for item in self)


class ArrayBag(AbstractBag):
    def __init__(self, sourceCollection=None):
        self.items = [None] * 10
        super().__init__(sourceCollection)

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
            raise KeyError(item)
        index = 0
        while self.items[index] != item:
            index += 1
        for cursor in range(index, len(self) - 1):
            self.items[cursor] = self.items[cursor + 1]
        self.size -= 1
        self.items[len(self)] = None


if __name__ == "__main__":
    bag = ArrayBag([1, 2, 2, 3])
    copy = bag.clone()
    print("Bag:", bag)
    print("Cópia igual e distinta:", bag == copy, bag is not copy)
