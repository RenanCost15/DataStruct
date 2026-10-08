"""Média, mediana e moda solicitadas no Projeto 7 do Capítulo 1."""


def _require_values(numbers):
    if not numbers:
        raise ValueError("A lista deve conter ao menos um número")


def mean(numbers):
    """Retorna a média aritmética de uma lista de números."""
    _require_values(numbers)
    return sum(numbers) / len(numbers)


def median(numbers):
    """Retorna a mediana de uma lista de números."""
    _require_values(numbers)
    ordered = sorted(numbers)
    middle = len(ordered) // 2
    if len(ordered) % 2 == 1:
        return ordered[middle]
    return (ordered[middle - 1] + ordered[middle]) / 2


def mode(numbers):
    """Retorna o primeiro valor que apresenta a maior frequência."""
    _require_values(numbers)
    frequencies = {}
    for number in numbers:
        frequencies[number] = frequencies.get(number, 0) + 1
    return max(frequencies, key=frequencies.get)
