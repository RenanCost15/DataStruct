"""Capítulo 3 — Projeto 4: exponenciação rápida recursiva."""


def expo(number, exponent):
    """Calcula a potência pela definição recursiva do enunciado.

    Complexidade temporal e profundidade da pilha: O(log exponent).
    """
    if not isinstance(exponent, int) or exponent < 0:
        raise ValueError("O expoente deve ser um inteiro não negativo")
    if exponent == 0:
        return 1
    if exponent % 2 == 1:
        return number * expo(number, exponent - 1)
    half = expo(number, exponent // 2)
    return half * half


def main():
    print("2 elevado a 10 =", expo(2, 10))
    print("Complexidade: O(log n), sendo n o expoente.")


if __name__ == "__main__":
    main()
