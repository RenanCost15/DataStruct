# Capítulo 1 — Funções aninhadas e de ordem superior, p. 22–24.


def factorial(n):
    """Retorna o fatorial de n."""

    def recurse(n, product):
        """Função auxiliar para calcular o fatorial."""
        if n == 1:
            return product
        else:
            return recurse(n - 1, n * product)

    return recurse(n, 1)


print(factorial(5))


def factorial(n, product=1):
    """Retorna o fatorial de n."""
    if n == 1:
        return product
    else:
        return factorial(n - 1, n * product)


print(factorial(5))

# Lista usada apenas para executar os trechos com map e filter.
oldList = [67, 0, 22]

newList = []
for number in oldList:
    newList.append(str(number))
print(newList)

print(list(map(str, oldList)))
newList = list(map(str, oldList))
print(newList)

newList = []
for number in oldList:
    if number > 0:
        newList.append(number)
print(newList)

# O livro pressupõe que a função isPositive já esteja definida.
# newList = list(filter(isPositive, oldList))

newList = list(filter(lambda number: number > 0, oldList))
print(newList)

import functools

product = functools.reduce(lambda x, y: x * y, range(1, 11))
print(product)
