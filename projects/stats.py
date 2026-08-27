# Capítulo 1 — Projects, questão 7, p. 35.


def mean(numbers):
    """Retorna a média de uma lista de números."""
    return sum(numbers) / len(numbers)


def median(numbers):
    """Retorna a mediana de uma lista de números."""
    numbers = sorted(numbers)
    midpoint = len(numbers) // 2
    if len(numbers) % 2 == 1:
        return numbers[midpoint]
    return (numbers[midpoint - 1] + numbers[midpoint]) / 2


def mode(numbers):
    """Retorna a moda de uma lista de números."""
    return max(numbers, key=numbers.count)
