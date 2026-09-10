"""Exercício 3.2 — Busca estimada em lista de nomes.

Uma modificação pode estimar o índice pela posição alfabética (ideia semelhante
à interpolation search), em vez de escolher sempre o meio. Ela pode reduzir o
número médio de comparações quando os nomes estão distribuídos de forma próxima
à hipótese usada pela estimativa. Porém não há garantia assintótica melhor: uma
estimativa ruim pode gerar partições desequilibradas e até degradar o pior caso.
A busca binária mantém O(log n) garantido em dados ordenados.
"""
RESPOSTA="Estimativa pode ajudar na média, mas não melhora a garantia O(log n) da busca binária."
print(RESPOSTA)
