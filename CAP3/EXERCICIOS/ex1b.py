"""Capítulo 3 — primeiro bloco, Exercício 2."""

try:
    from .ex1a import contar_iteracoes
except ImportError:
    from ex1a import contar_iteracoes


def main():
    sizes = (1000, 2000, 4000, 10_000, 100_000)
    print(f"{'Tamanho':>12}{'Iterações':>12}")
    for size in sizes:
        print(f"{size:>12d}{contar_iteracoes(size):>12d}")
    print(
        "\nConclusão: dobrar n acrescenta aproximadamente uma iteração; "
        "multiplicar n por 10 acrescenta aproximadamente log2(10) ≈ 3,32 "
        "iterações. A taxa de crescimento é O(log n)."
    )


if __name__ == "__main__":
    main()
