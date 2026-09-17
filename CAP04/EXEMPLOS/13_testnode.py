"""Capítulo 4 — tester da classe Node, p. 107 (PDF p. 125)."""
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parent))
from importlib import import_module
Node = import_module('11_node').Node
head = None
for count in range(1, 6):
    head = Node(count, head)
probe = head
while probe is not None:
    print(probe.data)
    probe = probe.next
