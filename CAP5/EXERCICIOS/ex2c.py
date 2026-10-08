"""Exercício 2.3 — Simplificar __init__ de ArrayBag chamando clear.

Uma forma é inicializar o mínimo exigido por `clear` e delegar a ela o estado
vazio; depois adicionar os itens da coleção-fonte. A ideia central é não duplicar
a lógica de inicialização.
"""
PSEUDOCODIGO = """self.items = Array(DEFAULT_CAPACITY)
self.size = 0
self.clear()
if sourceCollection:
    for item in sourceCollection:
        self.add(item)
"""
print(PSEUDOCODIGO)
