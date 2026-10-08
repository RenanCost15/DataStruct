"""Capítulo 4 — Projeto 9: inserção em estrutura simplesmente encadeada."""


class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def insert(item, position, head):
    """Insere item em position; posições além do fim significam anexar."""
    if head is None or position <= 0:
        return Node(item, head)
    probe = head
    index = 0
    while index < position - 1 and probe.next is not None:
        probe = probe.next
        index += 1
    probe.next = Node(item, probe.next)
    return head


def toList(head):
    result = []
    while head is not None:
        result.append(head.data)
        head = head.next
    return result


if __name__ == "__main__":
    head = Node(1, Node(3))
    head = insert(2, 1, head)
    head = insert(4, 99, head)
    print("Resultado esperado [1, 2, 3, 4]:", toList(head))
