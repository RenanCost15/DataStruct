# Capítulo 1 — Dicionários e correspondência de padrões, p. 18–19.

print({})
print({"name": "Ken"})
print({"name": "Ken", "age": 67})
print({"hobbies": ["reading", "running"]})

for key in {"name": "Ken", "age": 67}:
    print(key)

# O livro informa que colorTuple é recebido de um seletor de cores.
colorTuple = ((20, 40, 60), "#14283c")

rgbTuple = colorTuple[0]
hexString = colorTuple[1]
r = rgbTuple[0]
g = rgbTuple[1]
b = rgbTuple[2]

((r, g, b), hexString) = colorTuple
