"""Projeto 03 — calcular a distância total percorrida por uma bola com índice de quique 0,6.

Resolução completa e comentada em PT-BR.
"""

# Capítulo 1 — Projeto 3, p. 34 do livro / p. 52 do PDF.

height = float(input("Digite a altura inicial da bola: "))
bounces = int(input("Digite o número de quiques: "))

totalDistance = 0
for count in range(bounces):
    totalDistance += height
    height *= 0.6
    totalDistance += height

print("Distância total percorrida:", totalDistance)
