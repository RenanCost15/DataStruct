"""Capítulo 4 — testtwowaynode.py, p. 120–121 (PDF p. 138–139)."""
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parent))
from importlib import import_module
TwoWayNode = import_module('25_two_way_node').TwoWayNode
head = TwoWayNode(1)
tail = head
for data in range(2, 6):
    tail.next = TwoWayNode(data, tail)
    tail = tail.next
probe = tail
while probe is not None:
    print(probe.data)
    probe = probe.previous
