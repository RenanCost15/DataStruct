"""Capítulo 3 — Projeto 3: exponenciação por multiplicações sucessivas."""


def expo(number, exponent):
    """Retorna ``number`` elevado a ``exponent`` sem ``**`` nem ``pow``.

    Complexidade temporal: O(exponent). Espaço auxiliar: O(1).
    """
    if not isinstance(exponent, int) or exponent < 0:
        raise ValueError("O expoente deve ser um inteiro não negativo")
    result = 1
    for _ in range(exponent):
        result *= number
    return result


def main():
    print("2 elevado a 10 =", expo(2, 10))
    print("Complexidade: O(n), sendo n o expoente.")


if __name__ == "__main__":
    main()
