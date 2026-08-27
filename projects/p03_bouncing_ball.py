# Capítulo 1 — Projects, questão 3, p. 34.

height = float(input("Digite a altura inicial da bola: "))
bounces = int(input("Digite o número de quiques: "))

totalDistance = 0
for count in range(bounces):
    totalDistance += height
    height *= 0.6
    totalDistance += height

print("Distância total percorrida:", totalDistance)
