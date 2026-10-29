"""Exercício 2.5 — Onde pertence add e como Python o encontra?

`add` pertence às subclasses concretas (ou a uma classe intermediária que realmente saiba inserir). Quando um método herdado executa `self.add(item)`, `self` continua sendo o objeto concreto; o despacho dinâmico pesquisa pela MRO e encontra a implementação adequada da subclasse."""
print(__doc__)