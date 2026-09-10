"""Exercício 5.5 — Por que merge sort é O(n log n) no pior caso?

A lista é dividida aproximadamente pela metade até unidades: O(log n) níveis.
Em cada nível, o total de itens processados nas mesclagens é O(n). Portanto,
O(n) * O(log n) = O(n log n), independentemente da ordem inicial.
"""
print("Merge sort: O(n log n) no pior caso")
