"""Exercício 5.2 — Pior caso do quicksort.

Se o pivô escolhido acaba repetidamente como mínimo ou máximo, uma partição tem
n-1 itens e a outra zero, criando O(n) níveis e O(n²) trabalho. Para uma estratégia
de pivô vulnerável, uma ordenação adversária pode provocar isso. Exemplo conceitual:
[1,2,3,4,5,6,7,8,9,10] quando o pivô escolhido é sempre uma extremidade.
"""
print("Pior caso: O(n²)")
