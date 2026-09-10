"""Capítulo 3 — bubbleSortWithTweak, p. 66–67 (PDF p. 84–85)."""
def swap(lyst, i, j):
    temp = lyst[i]; lyst[i] = lyst[j]; lyst[j] = temp

def bubbleSortWithTweak(lyst):
    n = len(lyst)
    while n > 1:
        swapped = False
        i = 1
        while i < n:
            if lyst[i] < lyst[i - 1]:
                swap(lyst, i, i - 1)
                swapped = True
            i += 1
        if not swapped:
            return
        n -= 1
