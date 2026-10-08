"""Capítulo 3 — Projeto 2: inversão eficiente de uma lista."""


def reverse(lyst):
    """Inverte ``lyst`` no próprio lugar, sem usar ``list.reverse``.

    Complexidade temporal: O(n). Espaço auxiliar: O(1).
    Assim como ``list.reverse()``, a função não retorna uma nova lista.
    """
    left = 0
    right = len(lyst) - 1
    while left < right:
        lyst[left], lyst[right] = lyst[right], lyst[left]
        left += 1
        right -= 1


def main():
    values = [1, 2, 3, 4, 5]
    reverse(values)
    print(values)
    print("Complexidade temporal: O(n); espaço auxiliar: O(1).")


if __name__ == "__main__":
    main()
