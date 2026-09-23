"""Projeto 09 — Complexidade de add em ArraySortedBag.

Mesmo que a posição de inserção possa ser encontrada por busca binária O(log n),
os itens posteriores do array precisam ser deslocados para abrir uma célula.
No pior e no caso médio esse deslocamento é O(n); logo add é O(n).
"""
print("ArraySortedBag.add = O(n)")
