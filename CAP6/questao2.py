"""Capítulo 6 — Projeto 2: LinkedBag como subclasse de AbstractBag."""


class AbstractBag:
    """Código que independe da representação concreta da bag."""

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
        return "{" + ", ".join(map(str, self)) + "}"

    def __add__(self, other):
        result = type(self)(self)
        for item in other:
            result.add(item)
        return result

    def count(self, item):
        return sum(1 for current in self if current == item)

    def __eq__(self, other):
        if self is other:
            return True
        if type(self) is not type(other) or len(self) != len(other):
            return False
        return all(self.count(item) == other.count(item) for item in self)


class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedBag(AbstractBag):
    """Mantém apenas os métodos dependentes dos nós encadeados."""

    def __init__(self, sourceCollection=None):
        self.items = None
        super().__init__(sourceCollection)

    def __iter__(self):
        probe = self.items
        while probe is not None:
            yield probe.data
            probe = probe.next

    def clear(self):
        self.size = 0
        self.items = None

    def add(self, item):
        self.items = Node(item, self.items)
        self.size += 1

    def remove(self, item):
        if item not in self:
            raise KeyError(str(item) + " não está na bag")
        probe = self.items
        trailer = None
        while probe.data != item:
            trailer = probe
            probe = probe.next
        if trailer is None:
            self.items = probe.next
        else:
            trailer.next = probe.next
        self.size -= 1


if __name__ == "__main__":
    bag = LinkedBag([1, 2, 3])
    bag.remove(2)
    print("Subclasse de AbstractBag:", issubclass(LinkedBag, AbstractBag))
    print("Conteúdo restante:", bag)
