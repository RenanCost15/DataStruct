"""Projeto 01 — calcular diâmetro, circunferência, área e volume de uma esfera a partir do raio.

Resolução completa e comentada em PT-BR.
"""

# Capítulo 1 — Projeto 1, p. 33 do livro / p. 51 do PDF.

import math

radius = float(input("Digite o raio da esfera: "))

diameter = 2 * radius
circumference = 2 * math.pi * radius
surfaceArea = 4 * math.pi * radius ** 2
volume = 4 / 3 * math.pi * radius ** 3

print("Diâmetro:", diameter)
print("Circunferência:", circumference)
print("Área da superfície:", surfaceArea)
print("Volume:", volume)
