"""Capítulo 4 — Projeto 1: tamanho lógico separado da capacidade física."""


class Array:
    """Array didático com capacidade fixa e tamanho lógico."""

    def __init__(self, capacity, fillValue=None):
        self.items = [fillValue] * capacity
        self.logicalSize = 0

    def __len__(self):
        """Retorna a capacidade (tamanho físico), como pede o livro."""
        return len(self.items)

    def size(self):
        """Retorna o número de itens atualmente disponíveis ao usuário."""
        return self.logicalSize

    def __str__(self):
        return str(self.items)

    def __iter__(self):
        return iter(self.items)

    def __getitem__(self, index):
        return self.items[index]

    def __setitem__(self, index, newItem):
        self.items[index] = newItem


if __name__ == "__main__":
    array = Array(5, 0)
    print("Tamanho lógico esperado 0:", array.size())
    print("Tamanho físico esperado 5:", len(array))
