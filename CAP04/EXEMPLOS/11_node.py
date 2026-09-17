"""Capítulo 4 — definição da classe Node, p. 106 (PDF p. 124)."""
class Node(object):
    def __init__(self, data, next=None):
        """Instancia um Node cujo próximo é None por padrão."""
        self.data = data
        self.next = next

class TwoWayNode(Node):
    """Definida mais adiante no capítulo, p. 120 (PDF p. 138)."""
    def __init__(self, data, previous=None, next=None):
        Node.__init__(self, data, next)
        self.previous = previous
