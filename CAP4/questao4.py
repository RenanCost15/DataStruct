"""Capítulo 4 — Projeto 4: insert e pop com redimensionamento."""


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
        newCapacity = max(1, len(self.items) * 2)
        self.items.extend([self.fillValue] * (newCapacity - len(self.items)))

    def shrink(self):
        newCapacity = max(self.capacity, len(self.items) // 2,
                          self.logicalSize)
        self.items = self.items[:newCapacity]

    def insert(self, position, item):
        if self.logicalSize == len(self.items):
            self.grow()
        position = max(0, min(position, self.logicalSize))
        for index in range(self.logicalSize, position, -1):
            self.items[index] = self.items[index - 1]
        self.items[position] = item
        self.logicalSize += 1

    def pop(self, position):
        if not 0 <= position < self.size():
            raise IndexError("índice fora do tamanho lógico")
        item = self.items[position]
        for index in range(position, self.logicalSize - 1):
            self.items[index] = self.items[index + 1]
        self.logicalSize -= 1
        self.items[self.logicalSize] = self.fillValue
        if (self.logicalSize <= len(self.items) // 4
                and len(self.items) >= self.capacity * 2):
            self.shrink()
        return item

    def logicalItems(self):
        return self.items[:self.logicalSize]


if __name__ == "__main__":
    array = Array(2, 0)
    array.insert(0, 10)
    array.insert(1, 30)
    array.insert(1, 20)
    array.insert(99, 40)
    print("Após inserções:", array.logicalItems())
    print("Removido:", array.pop(1))
    print("Após pop:", array.logicalItems())
