"""Capítulo 4 — Projeto 3: métodos grow e shrink da classe Array."""


class Array:
    def __init__(self, capacity, fillValue=None):
        if capacity < 0:
            raise ValueError("a capacidade não pode ser negativa")
        self.items = [fillValue] * capacity
        self.logicalSize = 0
        self.capacity = capacity
        self.fillValue = fillValue

    def __len__(self):
        return len(self.items)

    def size(self):
        return self.logicalSize

    def __getitem__(self, index):
        if not 0 <= index < self.size():
            raise IndexError("índice fora do tamanho lógico")
        return self.items[index]

    def __setitem__(self, index, newItem):
        if not 0 <= index < self.size():
            raise IndexError("índice fora do tamanho lógico")
        self.items[index] = newItem

    def grow(self):
        """Duplica o tamanho físico e usa fillValue nas novas células."""
        newCapacity = max(1, len(self.items) * 2)
        self.items.extend([self.fillValue] * (newCapacity - len(self.items)))

    def shrink(self):
        """Reduz pela metade sem ficar abaixo da capacidade inicial."""
        newCapacity = max(self.capacity, len(self.items) // 2)
        newCapacity = max(newCapacity, self.logicalSize)
        self.items = self.items[:newCapacity]


if __name__ == "__main__":
    array = Array(2, 0)
    array.grow()
    print("Após grow:", array.items)
    array.shrink()
    print("Após shrink:", array.items)
