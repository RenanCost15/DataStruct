# Capítulo 1 — "Catching Exceptions", p. 24–25.

"""
Autor: Ken Lambert
Demonstra uma função que captura erros no formato de números durante a entrada.
"""


def safeIntegerInput(prompt):
    """Solicita um inteiro e o retorna se estiver bem formado. Caso contrário,
    exibe uma mensagem de erro e repete o processo."""
    inputString = input(prompt)
    try:
        number = int(inputString)
        return number
    except ValueError:
        print("Erro no formato do número:", inputString)
        return safeIntegerInput(prompt)


if __name__ == "__main__":
    age = safeIntegerInput("Digite sua idade: ")
    print("Sua idade é", age)
