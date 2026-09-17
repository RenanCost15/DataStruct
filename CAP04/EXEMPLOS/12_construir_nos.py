"""Capítulo 4 — criação e alteração explícita de links entre nós, p. 106–107 (PDF p. 124–125).
Todos os pequenos trechos consecutivos dessa demonstração estão reunidos aqui.
"""
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parent))
from importlib import import_module
Node = import_module('11_node').Node

# Apenas um link vazio.
node1 = None
# Um nó com dados e link vazio.
node2 = Node("A", None)
# Um nó com dados e link para node2.
node3 = Node("B", node2)

# O livro mostra as seguintes alterações de referência como exemplos adicionais:
node1 = node3
node1.next = node3
node1 = Node("C", node3)
node1 = Node("C", None)
node1.next = node3
