"""Capítulo 3 — Projeto 1 (p. 87 / PDF p. 105).
Enunciado em PT-BR: modifique a busca sequencial para uma lista ordenada, de modo que ela pare quando o alvo for menor que o item corrente. Informe melhor, pior e caso médio.
Resolução: melhor O(1), pior O(n), médio O(n).
"""
def sequentialSearch(target, lyst):
    position=0
    while position < len(lyst):
        if target == lyst[position]: return position
        if target < lyst[position]: return -1
        position += 1
    return -1
if __name__=='__main__':
    dados=[20,44,48,55,62,66,74]
    for alvo in (20,55,90): print(alvo,sequentialSearch(alvo,dados))
