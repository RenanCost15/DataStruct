"""Imprime tempos para tamanhos de problema que dobram, com um laço."""

import time


def medir(problem_size):
    """Executa o laço do exemplo e retorna o tempo decorrido."""
    start = time.time()
    work = 1
    for _ in range(problem_size):
        work += 1
        work -= 1
    return time.time() - start


def main():
    problem_size = 10_000_000
    print("%20s%16s" % ("Tamanho do problema", "Segundos"))
    for _ in range(5):
        elapsed = medir(problem_size)
        print("%20d%16.3f" % (problem_size, elapsed))
        problem_size *= 2


if __name__ == "__main__":
    main()
