"""Exercício 4.2 — Papel das trocas na análise de selection e bubble sort.

Comparações e trocas compõem o trabalho. Selection sort faz O(n²) comparações e
no máximo O(n) trocas; bubble sort pode fazer O(n²) trocas. Em Python, listas
armazenam referências, então trocar dois elementos é O(1) independentemente do
tamanho interno do objeto referenciado. Em um modelo que copiasse objetos inteiros,
o tamanho dos objetos também influenciaria a constante de custo.
"""
print(__doc__)
