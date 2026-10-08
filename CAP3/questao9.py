"""Capítulo 3 — Projeto 9: quicksort híbrido com insertion sort."""

from random import Random
from statistics import median
from time import perf_counter


def swap(lyst, i, j):
    lyst[i], lyst[j] = lyst[j], lyst[i]


def partition(lyst, left, right):
    middle = (left + right) // 2
    pivot = lyst[middle]
    lyst[middle] = lyst[right]
    lyst[right] = pivot
    boundary = left
    for index in range(left, right):
        if lyst[index] < pivot:
            swap(lyst, index, boundary)
            boundary += 1
    swap(lyst, right, boundary)
    return boundary


def insertionSortRange(lyst, left, right):
    """Ordena, por inserção, o intervalo inclusivo ``left..right``."""
    for i in range(left + 1, right + 1):
        item = lyst[i]
        j = i - 1
        while j >= left and lyst[j] > item:
            lyst[j + 1] = lyst[j]
            j -= 1
        lyst[j + 1] = item


def quicksort(lyst):
    quicksortHelper(lyst, 0, len(lyst) - 1)


def quicksortHelper(lyst, left, right):
    if left < right:
        pivot_location = partition(lyst, left, right)
        quicksortHelper(lyst, left, pivot_location - 1)
        quicksortHelper(lyst, pivot_location + 1, right)


def hybridQuicksort(lyst, threshold=50):
    if threshold < 2:
        raise ValueError("O limiar deve ser pelo menos 2")
    hybridQuicksortHelper(lyst, 0, len(lyst) - 1, threshold)


def hybridQuicksortHelper(lyst, left, right, threshold):
    if left >= right:
        return
    if right - left + 1 < threshold:
        insertionSortRange(lyst, left, right)
        return
    pivot_location = partition(lyst, left, right)
    hybridQuicksortHelper(lyst, left, pivot_location - 1, threshold)
    hybridQuicksortHelper(lyst, pivot_location + 1, right, threshold)


def _time_sort(sorter, data, repeats=7):
    timings = []
    for _ in range(repeats):
        sample = data.copy()
        start = perf_counter()
        sorter(sample)
        timings.append(perf_counter() - start)
        if sample != sorted(data):
            raise AssertionError("A ordenação produziu resultado incorreto")
    return median(timings)


def compare(sizes=(50, 500, 5000), threshold=50, repeats=7, seed=2026):
    """Compara o quicksort original e o híbrido nos tamanhos solicitados."""
    generator = Random(seed)
    rows = []
    for size in sizes:
        data = list(range(size))
        generator.shuffle(data)
        original = _time_sort(quicksort, data, repeats)
        hybrid = _time_sort(
            lambda values: hybridQuicksort(values, threshold), data, repeats
        )
        rows.append((size, original, hybrid))
    return rows


def findOptimalThreshold(
    size=5000,
    thresholds=(5, 10, 20, 30, 40, 50, 60, 75, 100),
    repeats=7,
    seed=2026,
):
    """Testa limiares e retorna todos os tempos e o melhor nesta máquina."""
    data = list(range(size))
    Random(seed).shuffle(data)
    rows = []
    for threshold in thresholds:
        elapsed = _time_sort(
            lambda values, t=threshold: hybridQuicksort(values, t),
            data,
            repeats,
        )
        rows.append((threshold, elapsed))
    return rows, min(rows, key=lambda row: row[1])


def main():
    print("Comparação (mediana de 7 execuções):")
    print(f"{'n':>8}{'Original (s)':>16}{'Híbrido 50 (s)':>18}")
    for size, original, hybrid in compare():
        print(f"{size:>8d}{original:>16.8f}{hybrid:>18.8f}")

    print("\nAjuste do limiar com n = 5000:")
    rows, best = findOptimalThreshold()
    print(f"{'Limiar':>10}{'Segundos':>14}")
    for threshold, elapsed in rows:
        print(f"{threshold:>10d}{elapsed:>14.8f}")
    print(f"Melhor limiar nesta execução: {best[0]} ({best[1]:.8f} s)")
    print("O valor ótimo depende do hardware e da implementação de Python.")


if __name__ == "__main__":
    main()
