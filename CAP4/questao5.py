"""Capítulo 4 — Projeto 5: igualdade entre objetos Array."""


class Array:
    def __init__(self, capacity, fillValue=None):
        self.items = [fillValue] * capacity
        self.logicalSize = 0

    def __len__(self):
        return len(self.items)

    def size(self):
        return self.logicalSize

    def append(self, item):
        if self.logicalSize == len(self.items):
            self.items.extend([None] * max(1, len(self.items)))
        self.items[self.logicalSize] = item
        self.logicalSize += 1

    def __getitem__(self, index):
        if not 0 <= index < self.size():
            raise IndexError("índice fora do tamanho lógico")
        return self.items[index]

    def __eq__(self, other):
        if not isinstance(other, Array) or self.size() != other.size():
            return False
        for index in range(self.size()):
            if self[index] != other[index]:
                return False
        return True


if __name__ == "__main__":
    left = Array(2)
    right = Array(5)
    different = Array(2)
    for value in (1, 2, 3):
        left.append(value)
        right.append(value)
    for value in (1, 3, 2):
        different.append(value)
    print("Arrays iguais (esperado True):", left == right)
    print("Ordem diferente (esperado False):", left == different)
