#!/usr/bin/env python3

import sys
import time
from make_array import aRandom, aBest, aWorse

def partition(v: list[int], s: int, e: int) -> int:
    d = s - 1
    for j in range(s, e):
        if v[j] <= v[e]:
            d += 1
            v[j], v[d] = v[d], v[j]
    v[e], v[(d + 1)] = v[(d + 1)], v[e]
    return (d + 1)

def quickSort(v: list[int], s: int, e: int):
    if (s < e):
        p = partition(v, s, e)
        quickSort(v, s, (p - 1))
        quickSort(v, (p + 1), e)

if __name__ == "__main__":
    input = int(sys.argv[1])
    
    # to random
    array = aRandom(input)

    # to worse
    # array = aWorse(input)

    e = len(array) - 1
    start = time.time_ns()
    quickSort(array, 0, e)
    end = time.time_ns()
    last_time = end - start
    print(last_time)
