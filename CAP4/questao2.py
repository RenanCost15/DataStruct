"""Capítulo 4 — Projeto 2: pré-condições de acesso e substituição."""


class Array:
    def __init__(self, capacity, fillValue=None):
        self.items = [fillValue] * capacity
        self.logicalSize = 0

    def __len__(self):
        return len(self.items)

    def size(self):
        return self.logicalSize

    def __str__(self):
        return str(self.items)

    def __iter__(self):
        return iter(self.items)

    def __getitem__(self, index):
        if not 0 <= index < self.size():
            raise IndexError("índice fora do tamanho lógico")
        return self.items[index]

    def __setitem__(self, index, newItem):
        if not 0 <= index < self.size():
            raise IndexError("índice fora do tamanho lógico")
        self.items[index] = newItem


if __name__ == "__main__":
    array = Array(3)
    array.logicalSize = 1
    array[0] = 10
    print("Item na posição lógica 0:", array[0])
    try:
        print(array[1])
    except IndexError as error:
        print("Exceção esperada:", error)
