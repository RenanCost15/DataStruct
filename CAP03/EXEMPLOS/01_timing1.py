"""Capítulo 3 — timing1.py, p. 51 (PDF p. 69).
Exibe tempos de execução para tamanhos de problema que dobram, usando um único laço.
"""
import time

problemSize = 10000000
print("%12s%16s" % ("Tamanho", "Segundos"))
for count in range(5):
    start = time.time()
    # Início do algoritmo medido.
    work = 1
    for x in range(problemSize):
        work += 1
        work -= 1
    # Fim do algoritmo medido.
    elapsed = time.time() - start
    print("%12d%16.3f" % (problemSize, elapsed))
    problemSize *= 2
