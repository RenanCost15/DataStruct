"""Capítulo 4 — estrutura circular com nó cabeçalho fictício, p. 119 (PDF p. 137).
Inclui a inicialização e o algoritmo de inserção apresentados no texto.
"""
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parent))
from importlib import import_module
Node = import_module('11_node').Node

head = Node(None, None)
head.next = head

# Exemplo do livro: insere após localizar o nó anterior à posição desejada.
index = 0
newItem = "A"
probe = head
while index > 0 and probe.next != head:
    probe = probe.next
    index -= 1
probe.next = Node(newItem, probe.next)
