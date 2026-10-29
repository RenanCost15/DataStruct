"""Exercício 1.3 — Como Python localiza remove em ArraySortedBag?

A busca de método segue a MRO: primeiro ArraySortedBag; se remove não estiver ali, segue para ArrayBag e depois ancestrais. Portanto a implementação herdada de remove é executada, enquanto chamadas internas como `item in self` podem despachar para o __contains__ redefinido na subclasse."""
print(__doc__)