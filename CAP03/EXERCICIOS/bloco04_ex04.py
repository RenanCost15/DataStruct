"""Exercício 4.4 — Por que insertion sort é bom em listas parcialmente ordenadas?

O custo principal é deslocar itens maiores que a chave. Se há poucas inversões,
há poucos deslocamentos; uma lista já ordenada exige apenas uma comparação por
posição e roda em O(n). Por isso ele é excelente para sublistas pequenas/quase
ordenadas e é usado como etapa auxiliar em algoritmos híbridos.
"""
print("Poucas inversões -> poucas movimentações.")
