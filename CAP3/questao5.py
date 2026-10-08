"""Capítulo 3 — Projeto 5: selection sort com argumento ``reverse``."""


def swap(lyst, i, j):
    lyst[i], lyst[j] = lyst[j], lyst[i]


def selectionSort(lyst, reverse=False):
    """Ordena ``lyst`` em ordem crescente ou, se pedido, decrescente."""
    for i in range(len(lyst) - 1):
        selected = i
        for j in range(i + 1, len(lyst)):
            if reverse:
                should_select = lyst[j] > lyst[selected]
            else:
                should_select = lyst[j] < lyst[selected]
            if should_select:
                selected = j
        if selected != i:
            swap(lyst, i, selected)


def main():
    ascending = [5, 1, 4, 2, 3]
    descending = ascending.copy()
    selectionSort(ascending)
    selectionSort(descending, reverse=True)
    print("Crescente:", ascending)
    print("Decrescente:", descending)


if __name__ == "__main__":
    main()
