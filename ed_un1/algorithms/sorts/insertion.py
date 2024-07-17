#!/usr/bin/env python3

import sys
import time
from make_array import aRandom, aBest, aWorse

def insertionSort(array: list[int], n):

    for i in range(1, n):
        while (i > 0) and array[i - 1] > array[i]:
            array[i], array[i - 1] = array[i - 1], array[i]
            i -= 1

if __name__ == "__main__":
    input = int(sys.argv[1])

    # to random 
    array = aRandom(input)

    # to worse
    # array = aWorse(input)

    # to best
    # array = arrayBest(input)

    n = len(array)
    start = time.time_ns()
    insertionSort(array, n)
    end = time.time_ns()
    last_time = end - start
    print(last_time)
