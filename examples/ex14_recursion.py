# Capítulo 1 — "Recursive Functions", p. 20–22.


def displayRange(lower, upper):
    """Exibe os números do limite inferior ao superior."""
    while lower <= upper:
        print(lower)
        lower = lower + 1


displayRange(1, 4)


def displayRange(lower, upper):
    """Exibe os números do limite inferior ao superior."""
    if lower <= upper:
        print(lower)
        displayRange(lower + 1, upper)


displayRange(1, 4)


def ourSum(lower, upper):
    """Retorna a soma dos números do limite inferior ao superior."""
    if lower > upper:
        return 0
    else:
        return lower + ourSum(lower + 1, upper)


print(ourSum(1, 4))


def ourSum(lower, upper, margin=0):
    """Retorna a soma e exibe o rastreamento dos argumentos e retornos."""
    blanks = " " * margin
    print(blanks, lower, upper)
    if lower > upper:
        print(blanks, 0)
        return 0
    else:
        result = lower + ourSum(lower + 1, upper, margin + 4)
        print(blanks, result)
        return result


print(ourSum(1, 4))
