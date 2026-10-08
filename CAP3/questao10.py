"""Capítulo 3 — Projeto 10: memória de fatorial e Fibonacci recursivos."""


def factorial(n):
    if n < 2:
        return 1
    return n * factorial(n - 1)


def fibonacci(n):
    if n < 3:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


def complexidades_memoria():
    """Retorna a análise pedida pelo enunciado."""
    return {
        "fatorial": "O(n)",
        "fibonacci": "O(n)",
        "justificativa": (
            "Cada quadro da pilha usa espaço constante e a profundidade "
            "máxima das duas recursões é proporcional a n. Fibonacci faz "
            "O(2^n) chamadas no total, mas elas não permanecem todas ativas "
            "simultaneamente; por isso o pico de memória da pilha é O(n)."
        ),
    }


def main():
    analysis = complexidades_memoria()
    print("Fatorial recursivo:", analysis["fatorial"])
    print("Fibonacci recursivo:", analysis["fibonacci"])
    print(analysis["justificativa"])


if __name__ == "__main__":
    main()
