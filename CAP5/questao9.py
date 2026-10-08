"""Capítulo 5 — Projeto 9: custo de ArraySortedBag.add.

A posição de inserção pode ser localizada em O(log n) com busca binária, mas
abrir uma célula no array exige deslocar até n itens. Um redimensionamento
ocasional também copia n itens. Portanto, o tempo de pior caso de ``add`` é
O(n), e o deslocamento mantém linear o custo médio de uma inserção em posição
arbitrária.
"""


if __name__ == "__main__":
    print("ArraySortedBag.add: O(n)")
