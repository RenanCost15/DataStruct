# Capítulo 1 — Projects, questão 1, p. 33.

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
