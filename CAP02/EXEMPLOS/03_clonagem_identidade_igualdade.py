"""Capítulo 2 — Exemplo do livro, p. 43 (PDF p. 61).
Cópia rasa de lista e diferença entre identidade (is) e igualdade estrutural (==).
"""
lyst1 = [2, 4, 8]
lyst2 = list(lyst1)
print(lyst1 is lyst2)  # False
print(lyst1 == lyst2)  # True
