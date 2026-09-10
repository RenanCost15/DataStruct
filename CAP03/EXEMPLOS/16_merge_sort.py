"""Capítulo 3 — implementação de merge sort, p. 74–76 (PDF p. 92–94).
O livro usa um buffer temporário e chamadas recursivas para dividir e intercalar a lista.
"""
def mergeSort(lyst):
    copyBuffer = [None] * len(lyst)
    mergeSortHelper(lyst, copyBuffer, 0, len(lyst) - 1)

def mergeSortHelper(lyst, copyBuffer, low, high):
    if low < high:
        middle = (low + high) // 2
        mergeSortHelper(lyst, copyBuffer, low, middle)
        mergeSortHelper(lyst, copyBuffer, middle + 1, high)
        merge(lyst, copyBuffer, low, middle, high)

def merge(lyst, copyBuffer, low, middle, high):
    i1 = low
    i2 = middle + 1
    for i in range(low, high + 1):
        if i1 > middle:
            copyBuffer[i] = lyst[i2]; i2 += 1
        elif i2 > high:
            copyBuffer[i] = lyst[i1]; i1 += 1
        elif lyst[i1] < lyst[i2]:
            copyBuffer[i] = lyst[i1]; i1 += 1
        else:
            copyBuffer[i] = lyst[i2]; i2 += 1
    for i in range(low, high + 1):
        lyst[i] = copyBuffer[i]
