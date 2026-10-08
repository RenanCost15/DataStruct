"""Capítulo 4 — Projeto 8: função length para estrutura encadeada."""


class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def length(head):
    """Retorna o número de itens da estrutura simplesmente encadeada."""
    count = 0
    probe = head
    while probe is not None:
        count += 1
        probe = probe.next
    return count


if __name__ == "__main__":
    head = Node(1, Node(2, Node(3)))
    print("Comprimento esperado 3:", length(head))
    print("Comprimento da estrutura vazia esperado 0:", length(None))
