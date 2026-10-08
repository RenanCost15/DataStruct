"""Capítulo 1 — Projeto 4: aproximação de pi pela série de Leibniz."""


def aproximar_pi(iteracoes):
    """Calcula ``4 * (1 - 1/3 + 1/5 - 1/7 + ...)``."""
    if iteracoes < 1:
        raise ValueError("O número de iterações deve ser positivo")
    soma = 0.0
    sinal = 1.0
    denominador = 1
    for _ in range(iteracoes):
        soma += sinal / denominador
        sinal *= -1
        denominador += 2
    return 4 * soma


def main():
    iteracoes = int(input("Número de iterações: "))
    print(f"Valor aproximado de pi: {aproximar_pi(iteracoes):.15f}")


if __name__ == "__main__":
    main()
