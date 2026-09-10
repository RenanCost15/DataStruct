"""Capítulo 3 — Estudo de caso: Um Profiler de Algoritmos, p. 82 (PDF p. 100).
Módulo algorithms.py configurado para o profiler.
"""
def selectionSort(lyst, profiler):
    i = 0
    while i < len(lyst) - 1:
        minIndex = i
        j = i + 1
        while j < len(lyst):
            profiler.comparison()          # Conta a comparação.
            if lyst[j] < lyst[minIndex]:
                minIndex = j
            j += 1
        if minIndex != i:
            swap(lyst, minIndex, i, profiler)
        i += 1

def swap(lyst, i, j, profiler):
    """Troca os elementos nas posições i e j."""
    profiler.exchange()                    # Conta a troca.
    temp = lyst[i]
    lyst[i] = lyst[j]
    lyst[j] = temp
