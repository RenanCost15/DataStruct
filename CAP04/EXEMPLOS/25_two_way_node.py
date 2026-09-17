"""Capítulo 4 — TwoWayNode, p. 120 (PDF p. 138)."""
class Node(object):
    def __init__(self, data, next=None): self.data=data; self.next=next
class TwoWayNode(Node):
    def __init__(self, data, previous=None, next=None):
        Node.__init__(self, data, next)
        self.previous = previous
