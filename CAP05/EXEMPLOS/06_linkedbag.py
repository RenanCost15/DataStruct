"""Capítulo 5 — LinkedBag desenvolvido nas p. 139–141 (PDF p. 157–159).
Reúne as partes que o livro acrescenta progressivamente.
"""
from pathlib import Path
import sys, importlib
cap4 = Path(__file__).resolve().parents[2] / 'CAP04' / 'EXEMPLOS'
sys.path.insert(0, str(cap4))
Node = importlib.import_module('11_node').Node

class LinkedBag(object):
    def __init__(self, sourceCollection=None):
        self.items = None
        self.size = 0
        if sourceCollection:
            for item in sourceCollection: self.add(item)
    def isEmpty(self): return len(self) == 0
    def __len__(self): return self.size
    def __iter__(self):
        cursor = self.items
        while cursor is not None:
            yield cursor.data
            cursor = cursor.next
    def __str__(self): return '{' + ', '.join(map(str, self)) + '}'
    def count(self,item): return sum(1 for x in self if x==item)
    def __add__(self,other):
        result=LinkedBag(self)
        for item in other: result.add(item)
        return result
    def __eq__(self,other):
        if self is other: return True
        if type(self)!=type(other) or len(self)!=len(other): return False
        return all(self.count(x)==other.count(x) for x in self)
    def clear(self): self.items=None; self.size=0
    def add(self, item):
        self.items = Node(item, self.items)
        self.size += 1
    def remove(self, item):
        if item not in self: raise KeyError(str(item) + ' não está na bag')
        probe = self.items; trailer = None
        for targetItem in self:
            if targetItem == item: break
            trailer = probe; probe = probe.next
        if probe == self.items: self.items = self.items.next
        else: trailer.next = probe.next
        self.size -= 1
