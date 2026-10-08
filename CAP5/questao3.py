"""Capítulo 5 — Projeto 3: ArrayBag.add com redimensionamento."""


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
        """Duplica o array quando o tamanho lógico alcança a capacidade."""
        if len(self) == len(self.items):
            newItems = [None] * (len(self.items) * 2)
            for index in range(len(self)):
                newItems[index] = self.items[index]
            self.items = newItems
        self.items[len(self)] = item
        self.size += 1


if __name__ == "__main__":
    bag = ArrayBag(range(25))
    print("Tamanho lógico esperado 25:", len(bag))
    print("Capacidade após crescer:", len(bag.items))
    print("Itens preservados:", list(bag))
