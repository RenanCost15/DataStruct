"""Exercício 2.4 — Implementar clone em AbstractCollection.

Usar `type(self)(self)` preserva o tipo concreto e reutiliza o construtor que
aceita uma coleção-fonte.
"""
class Exemplo:
    def __init__(self, fonte=None): self.dados=list(fonte or [])
    def __iter__(self): return iter(self.dados)
    def clone(self): return type(self)(self)
a=Exemplo([1,2,3]); b=a.clone(); print(a.dados,b.dados,a is b)
