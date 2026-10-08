"""Capítulo 3 — primeiro bloco, Exercício 1."""


def contar_iteracoes(problem_size):
    """Conta quantas vezes o laço divide o tamanho do problema por 2."""
    if problem_size < 0:
        raise ValueError("O tamanho do problema não pode ser negativo")
    iterations = 0
    while problem_size > 0:
        problem_size //= 2
        iterations += 1
    return iterations


def main():
    problem_size = int(input("Tamanho do problema: "))
    print("Número de iterações:", contar_iteracoes(problem_size))


if __name__ == "__main__":
    main()
