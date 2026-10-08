"""Funções recursivas apresentadas no Capítulo 1."""


def square(n):
    """Retorna o quadrado de ``n``."""
    result = n ** 2
    return result


def displayRange(lower, upper):
    """Exibe os números de ``lower`` até ``upper``, inclusive."""
    if lower <= upper:
        print(lower)
        displayRange(lower + 1, upper)


def ourSum(lower, upper, margin=0):
    """Soma o intervalo e exibe o rastro das chamadas e dos retornos."""
    blanks = " " * margin
    print(blanks, lower, upper)
    if lower > upper:
        print(blanks, 0)
        return 0
    result = lower + ourSum(lower + 1, upper, margin + 4)
    print(blanks, result)
    return result


def factorial_nested(n):
    """Retorna ``n!`` usando a função auxiliar aninhada do exemplo."""
    if n < 1:
        raise ValueError("n deve ser um inteiro positivo")

    def recurse(value, product):
        if value == 1:
            return product
        return recurse(value - 1, value * product)

    return recurse(n, 1)


def factorial(n, product=1):
    """Retorna ``n!`` pela segunda definição recursiva do exemplo."""
    if n < 1:
        raise ValueError("n deve ser um inteiro positivo")
    if n == 1:
        return product
    return factorial(n - 1, n * product)


if __name__ == "__main__":
    print("displayRange(1, 4):")
    displayRange(1, 4)
    print("\nourSum(1, 4):")
    print("Resultado:", ourSum(1, 4))
    print("\nfactorial_nested(5):", factorial_nested(5))
    print("factorial(5):", factorial(5))
