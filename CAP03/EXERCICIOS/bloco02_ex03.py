"""Exercício 2.3 — Quando n^4 passa a ser melhor do que 2^n?

Em n=16 há empate: 16^4 = 2^16 = 65536. A partir de n=17, n^4 < 2^n
e a vantagem do algoritmo polinomial cresce rapidamente.
"""
for n in range(14,19):
    print(n, n**4, 2**n, "n^4 melhor?", n**4 < 2**n)
