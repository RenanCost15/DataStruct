"""Capítulo 3 — counting.py, p. 53 (PDF p. 71).
Exibe o número de iterações para tamanhos de problema que dobram, usando laços aninhados.
"""
problemSize = 1000
print("%12s%15s" % ("Tamanho", "Iterações"))
for count in range(5):
    number = 0
    work = 1
    for j in range(problemSize):
        for k in range(problemSize):
            number += 1
            work += 1
            work -= 1
    print("%12d%15d" % (problemSize, number))
    problemSize *= 2
