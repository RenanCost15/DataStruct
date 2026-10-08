"""Capítulo 3 — Projeto 6: Fibonacci recursivo com memoização."""

from pathlib import Path
import sys

COUNTER_DIRECTORY = Path(__file__).resolve().parents[1] / "CAP1" / "EXEMPLOS"
if str(COUNTER_DIRECTORY) not in sys.path:
    sys.path.insert(0, str(COUNTER_DIRECTORY))

from counter import Counter


def fib(n, memo, counter):
    """Retorna Fibonacci(n), memoriza resultados e conta chamadas."""
    if not isinstance(n, int) or n < 1:
        raise ValueError("n deve ser um inteiro positivo")
    counter.increment()
    if n in memo:
        return memo[n]
    if n < 3:
        result = 1
    else:
        result = fib(n - 1, memo, counter) + fib(n - 2, memo, counter)
    memo[n] = result
    return result


def fibonacci_com_perfil(n):
    memo = {}
    counter = Counter()
    result = fib(n, memo, counter)
    return result, counter.getValue(), memo


def main():
    n = 16
    result, calls, memo = fibonacci_com_perfil(n)
    print(f"fib({n}) = {result}")
    print("Chamadas:", calls)
    print("Dicionário:", memo)
    print("Tempo e espaço: O(n).")


if __name__ == "__main__":
    main()
