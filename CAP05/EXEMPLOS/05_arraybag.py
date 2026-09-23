"""Capítulo 5 — ArrayBag desenvolvido nas p. 134–138 (PDF p. 152–156).
Reúne num único módulo as partes que o livro acrescenta progressivamente.
"""
from pathlib import Path
import sys, importlib
cap4 = Path(__file__).resolve().parents[2] / 'CAP04' / 'EXEMPLOS'
sys.path.insert(0, str(cap4))
Array = importlib.import_module('01_arrays').Array

class ArrayBag(object):
    DEFAULT_CAPACITY = 10
    def __init__(self, sourceCollection=None):
        self.items = Array(ArrayBag.DEFAULT_CAPACITY)
        self.size = 0
        if sourceCollection:
            for item in sourceCollection: self.add(item)
    def isEmpty(self): return len(self) == 0
    def __len__(self): return self.size
    def clear(self):
        self.size = 0
        self.items = Array(ArrayBag.DEFAULT_CAPACITY)
    def add(self, item):
        # O livro marca aqui o ponto onde o redimensionamento será acrescentado em projeto.
        self.items[len(self)] = item
        self.size += 1
    def __iter__(self):
        cursor = 0
        while cursor < len(self):
            yield self.items[cursor]
            cursor += 1
    def __str__(self): return '{' + ', '.join(map(str, self)) + '}'
    def __add__(self, other):
        result = ArrayBag(self)
        for item in other: result.add(item)
        return result
    def count(self, item): return sum(1 for x in self if x == item)
    def __eq__(self, other):
        if self is other: return True
        if type(self) != type(other) or len(self) != len(other): return False
        for item in self:
            if self.count(item) != other.count(item): return False
        return True
    def remove(self, item):
        if item not in self: raise KeyError(str(item) + ' não está na bag')
        targetIndex = 0
        for targetItem in self:
            if targetItem == item: break
            targetIndex += 1
        for i in range(targetIndex, len(self) - 1):
            self.items[i] = self.items[i + 1]
        self.size -= 1
        # O redimensionamento para baixo é deixado para projeto no livro.
