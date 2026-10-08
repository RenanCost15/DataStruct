"""Capítulo 5 — Projeto 7: conjunto LinkedSet baseado em nós."""


class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedBag:
    def __init__(self, sourceCollection=None):
        self.items = None
        self.size = 0
        if sourceCollection:
            for item in sourceCollection:
                self.add(item)

    def __len__(self):
        return self.size

    def __iter__(self):
        probe = self.items
        while probe is not None:
            yield probe.data
            probe = probe.next

    def add(self, item):
        self.items = Node(item, self.items)
        self.size += 1

    def remove(self, item):
        probe = self.items
        trailer = None
        while probe is not None and probe.data != item:
            trailer = probe
            probe = probe.next
        if probe is None:
            raise KeyError(item)
        if trailer is None:
            self.items = probe.next
        else:
            trailer.next = probe.next
        self.size -= 1


class LinkedSet(LinkedBag):
    """Tem a interface da bag, mas ignora inclusões duplicadas."""

    def add(self, item):
        if item not in self:
            super().add(item)


if __name__ == "__main__":
    collection = LinkedSet([3, 1, 3, 2, 2])
    print("Itens únicos:", list(collection))
    print("Tamanho esperado 3:", len(collection))
