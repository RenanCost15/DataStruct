"""Projeto 04 — aproximar π pela série de Leibniz para um número informado de iterações.

Resolução completa e comentada em PT-BR.
"""

# Capítulo 1 — Projeto 4, p. 34 do livro / p. 52 do PDF.

iterations = int(input("Digite o número de iterações: "))

approximation = 0
for count in range(iterations):
    approximation += (-1) ** count / (2 * count + 1)

print("Valor aproximado de pi:", approximation * 4)
