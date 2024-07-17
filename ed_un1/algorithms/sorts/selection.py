#!/usr/bin/env python3

import sys
import time
from make_array import aRandom, aBest, aWorse

def selectionSort(array: list[int], n: int):

    for i in range(0, (n - 1)):
        m = i

        for j in range(i + 1, n):

            if array[j] < array[m]:
                m = j

        array[i], array[m] = array[m], array[i]

if __name__ == "__main__":
    input = int(sys.argv[1])
    array = aRandom(input)
    n = len(array)
    start = time.time_ns()
    selectionSort(array, n)
    end = time.time_ns()
    last_time = end - start
    print(last_time)
