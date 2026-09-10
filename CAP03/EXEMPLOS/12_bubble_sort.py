"""Capítulo 3 — bubbleSort, p. 66 (PDF p. 84)."""
def swap(lyst, i, j):
    temp = lyst[i]; lyst[i] = lyst[j]; lyst[j] = temp

def bubbleSort(lyst):
    n = len(lyst)
    while n > 1:
        i = 1
        while i < n:
            if lyst[i] < lyst[i - 1]:
                swap(lyst, i, i - 1)
            i += 1
        n -= 1
