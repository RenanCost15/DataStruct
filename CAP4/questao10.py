"""Capítulo 4 — Projeto 10: remoção em estrutura simplesmente encadeada."""


class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def length(head):
    count = 0
    while head is not None:
        count += 1
        head = head.next
    return count


def pop(position, head):
    """Retorna (estrutura modificada, item removido)."""
    if not 0 <= position < length(head):
        raise IndexError("posição fora da estrutura")
    if position == 0:
        return head.next, head.data
    probe = head
    for _ in range(position - 1):
        probe = probe.next
    removed = probe.next
    probe.next = removed.next
    return head, removed.data


def toList(head):
    result = []
    while head is not None:
        result.append(head.data)
        head = head.next
    return result


if __name__ == "__main__":
    head = Node(1, Node(2, Node(3)))
    head, item = pop(1, head)
    print("Item removido esperado 2:", item)
    print("Estrutura esperada [1, 3]:", toList(head))
