# Capítulo 1 — Atribuições, importações e ajuda, p. 8–10.

PI = 3.1416
minValue, maxValue = 1, 100

# Valores apenas para permitir a troca mostrada pelo livro.
a, b = 10, 20
a, b = b, a

minValue = min(
    100,
    200,
)
product = max(100, 200) \
    * 30

import math

print(math.sqrt(2))

from math import sqrt

print(sqrt(2))

from math import pi, sqrt

print(sqrt(2) * pi)

print(dir(int))
print(dir(math))
help(abs)
help(math.sqrt)
