"""Capítulo 3 — conversão de Fibonacci para algoritmo linear, p. 79 (PDF p. 97)."""
def fib(n):
    if n < 3:
        return 1
    first = 1
    second = 1
    for count in range(3, n + 1):
        third = first + second
        first = second
        second = third
    return second
