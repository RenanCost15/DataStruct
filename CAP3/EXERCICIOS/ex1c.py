"""Capítulo 3 — primeiro bloco, Exercício 3."""

import time


def medir_tempo_de_cpu(problem_size):
    """Mede apenas o tempo de CPU consumido pelo processo atual.

    ``time.process_time()`` soma os tempos de CPU de usuário e de sistema e
    exclui períodos em que o processo fica suspenso, como durante ``sleep``.
    Somente a diferença entre duas chamadas tem significado.
    """
    start = time.process_time()
    work = 1
    for _ in range(problem_size):
        work += 1
        work -= 1
    return time.process_time() - start


def main():
    problem_size = 1_000_000
    print("Tempo de CPU:", medir_tempo_de_cpu(problem_size), "segundos")


if __name__ == "__main__":
    main()
