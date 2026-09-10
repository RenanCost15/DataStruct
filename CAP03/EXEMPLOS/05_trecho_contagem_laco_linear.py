"""Capítulo 3 — trecho retomado na análise de complexidade, p. 58 (PDF p. 76).
O livro usa este laço para ilustrar a contagem de trabalho linear.
"""
# problemSize é o tamanho do problema no contexto do exemplo.
problemSize = 10
work = 1
for x in range(problemSize):
    work += 1
    work -= 1
