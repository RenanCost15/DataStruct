#!/usr/bin/env python3

from random import randint

def aRandom (n):
    array = []

    for i in range(0, n):
        array.append(randint(1, 10000))

    return array

def aWorse (n):
    array = []

    for i in range(n, -1, -1):
        array.append(i)

    return array

def aBest (n):
    array = []

    for i in range(n):
        array.append(i)

    return array
