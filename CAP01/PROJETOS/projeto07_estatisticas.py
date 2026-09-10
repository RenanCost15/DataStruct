"""Projeto 07 — implementar média, mediana e moda em um módulo de estatística.

Resolução completa e comentada em PT-BR.
"""

# Capítulo 1 — Projeto 7, p. 35 do livro / p. 53 do PDF.


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
