"""Capítulo 5 — Projeto 6: conjunto ArraySet baseado em array."""


class ArrayBag:
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


class ArraySet(ArrayBag):
    """Tem a interface da bag, mas ignora inclusões duplicadas."""

    def add(self, item):
        if item not in self:
            super().add(item)


if __name__ == "__main__":
    collection = ArraySet([3, 1, 3, 2, 2])
    print("Itens únicos:", list(collection))
    print("Tamanho esperado 3:", len(collection))
