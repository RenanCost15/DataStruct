"""Capítulo 3 — Projeto 7: perfil do Fibonacci memoizado."""

from time import perf_counter

try:
    from .questao6 import fibonacci_com_perfil
except ImportError:
    from questao6 import fibonacci_com_perfil


def profile(sizes):
    """Retorna tamanho, chamadas, tempo e valor para cada teste."""
    rows = []
    for size in sizes:
        start = perf_counter()
        value, calls, _ = fibonacci_com_perfil(size)
        elapsed = perf_counter() - start
        rows.append((size, calls, elapsed, value))
    return rows


def main():
    sizes = (8, 16, 32, 64, 128, 256, 512)
    print(f"{'n':>6}{'Chamadas':>12}{'Segundos':>14}")
    for size, calls, elapsed, _ in profile(sizes):
        print(f"{size:>6d}{calls:>12d}{elapsed:>14.8f}")
    print(
        "Complexidade: O(n). Cada argumento de 1 a n é calculado apenas uma "
        "vez; consultas repetidas ao dicionário custam O(1) em média."
    )


if __name__ == "__main__":
    main()
