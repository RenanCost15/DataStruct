#!/usr/bin/env python3

import sys
import time
from make_array import aRandom, aBest, aWorse

def distributionSort(array: list[int], n):
    maiorElemento = max(array)
    arrayAux = [0] * (maiorElemento + 1)
    arrayResultante = [0] * n

    for i in range(n):
        arrayAux[array[i]] += 1

    for i in range(1, maiorElemento + 1):
        arrayAux[i] += arrayAux[i - 1]

    for i in range(n - 1, -1, -1):
        arrayResultante[arrayAux[array[i]] - 1] = array[i]
        arrayAux[array[i]] -= 1

    for i in range(n):
        array[i] = arrayResultante[i]

if __name__ == "__main__":
    input = int(sys.argv[1])
    array = aRandom(input)
    n = len(array)
    start = time.time_ns()
    distributionSort(array, n)
    end = time.time_ns()
    last_time = end - start
    print(last_time)
