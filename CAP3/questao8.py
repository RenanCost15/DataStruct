"""Capítulo 3 — Projeto 8: análise de ``makeRandomList``.

Sob as hipóteses do enunciado, a busca ``number in lyst`` visita até O(n)
itens e é repetida para os n elementos acrescentados. Portanto, o tempo
esperado é O(n²). O espaço da lista é O(n). Como o laço interno é probabilístico,
sem a hipótese sobre duplicatas não existe um limite determinístico finito para
o número de tentativas; a classificação O(n²) é a análise esperada solicitada.
"""

import random


def makeRandomList(size):
    lyst = []
    for _ in range(size):
        while True:
            number = random.randint(1, size)
            if number not in lyst:
                lyst.append(number)
                break
    return lyst


def main():
    print(makeRandomList(10))
    print("Complexidade temporal esperada: O(n²); espaço: O(n).")


if __name__ == "__main__":
    main()
