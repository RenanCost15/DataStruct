"""Conta iterações para tamanhos que dobram, usando laços aninhados."""


def contar_iteracoes(problem_size):
    """Executa e conta as iterações do laço interno do exemplo."""
    number = 0
    work = 1
    for _ in range(problem_size):
        for _ in range(problem_size):
            number += 1
            work += 1
            work -= 1
    return number


def main():
    problem_size = 1000
    print("%20s%15s" % ("Tamanho do problema", "Iterações"))
    for _ in range(5):
        number = contar_iteracoes(problem_size)
        print("%20d%15d" % (problem_size, number))
        problem_size *= 2


if __name__ == "__main__":
    main()
