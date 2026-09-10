"""Capítulo 3 — Fibonacci recursivo exponencial, p. 77 (PDF p. 95)."""
def fib(n):
    if n < 3:
        return 1
    return fib(n - 1) + fib(n - 2)
