"""Capítulo 3 — Projeto 1: busca sequencial em lista ordenada."""


def sequentialSearch(target, sortedLyst):
    """Retorna a posição do alvo ou -1, encerrando a busca antecipadamente."""
    position = 0
    while position < len(sortedLyst):
        if target == sortedLyst[position]:
            return position
        if target < sortedLyst[position]:
            return -1
        position += 1
    return -1


def main():
    values = [10, 20, 30, 40, 50]
    for target in (10, 35, 50, 60):
        print(target, "->", sequentialSearch(target, values))
    print("Melhor caso: O(1); caso médio: O(n); pior caso: O(n).")


if __name__ == "__main__":
    main()
