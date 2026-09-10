"""Exercício 5.4 — Quicksort híbrido com insertion sort.

Em sublistas pequenas, o custo da recursão e do particionamento pode superar o
benefício assintótico. Insertion sort tem implementação simples, boa localidade e
ótimo desempenho em blocos pequenos/quase ordenados. Um limiar cria um algoritmo
híbrido mais rápido na prática sem alterar O(n log n) médio.
"""
print("Híbrido reduz constantes de execução em sublistas pequenas.")
