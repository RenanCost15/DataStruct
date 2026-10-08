"""Capítulo 5 — Projeto 5: clone em ArrayBag e LinkedBag."""


class BagOperations:
    def __len__(self):
        return self.size

    def clone(self):
        """Retorna outra bag do mesmo tipo e com os mesmos itens."""
        return type(self)(self)

    def count(self, item):
        return sum(1 for current in self if current == item)

    def __eq__(self, other):
        if type(self) is not type(other) or len(self) != len(other):
            return False
        return all(self.count(item) == other.count(item) for item in self)


class ArrayBag(BagOperations):
    def __init__(self, sourceCollection=None):
        self.items = [None] * 10
        self.size = 0
        if sourceCollection:
            for item in sourceCollection:
                self.add(item)

    def __iter__(self):
        for index in range(len(self)):
            yield self.items[index]

    def add(self, item):
        if len(self) == len(self.items):
            self.items.extend([None] * len(self.items))
        self.items[len(self)] = item
        self.size += 1


class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedBag(BagOperations):
    def __init__(self, sourceCollection=None):
        self.items = None
        self.size = 0
        if sourceCollection:
            for item in sourceCollection:
                self.add(item)

    def __iter__(self):
        probe = self.items
        while probe is not None:
            yield probe.data
            probe = probe.next

    def add(self, item):
        self.items = Node(item, self.items)
        self.size += 1


if __name__ == "__main__":
    for bagType in (ArrayBag, LinkedBag):
        bag1 = bagType([2, 3, 4])
        bag2 = bag1.clone()
        print(bagType.__name__, bag1 == bag2, bag1 is bag2)
