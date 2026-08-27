# Capítulo 1 — Projects, questão 4, p. 34.

iterations = int(input("Digite o número de iterações: "))

approximation = 0
for count in range(iterations):
    approximation += (-1) ** count / (2 * count + 1)

print("Valor aproximado de pi:", approximation * 4)
