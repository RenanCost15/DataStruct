"""Capítulo 4 — Projeto 11: conversão para estrutura duplamente encadeada."""


class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class TwoWayNode(Node):
    def __init__(self, data, previous=None, next=None):
        super().__init__(data, next)
        self.previous = previous


def makeTwoWay(head):
    """Cria uma cópia duplamente encadeada sem alterar a origem."""
    newHead = None
    tail = None
    probe = head
    while probe is not None:
        newNode = TwoWayNode(probe.data, tail)
        if newHead is None:
            newHead = newNode
        else:
            tail.next = newNode
        tail = newNode
        probe = probe.next
    return newHead


if __name__ == "__main__":
    original = Node(1, Node(2, Node(3)))
    copy = makeTwoWay(original)
    print(copy.data, copy.next.data, copy.next.next.data)
    print("Vínculo anterior esperado 2:", copy.next.next.previous.data)
    print("Origem não alterada:", not hasattr(original, "previous"))
