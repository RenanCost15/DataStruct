"""Demonstra uma função que trata erros de formato numérico na entrada."""


def safeIntegerInput(prompt):
    """Solicita e retorna um inteiro; repete após uma entrada inválida."""
    input_string = input(prompt)
    try:
        return int(input_string)
    except ValueError:
        print("Erro no formato do número:", input_string)
        return safeIntegerInput(prompt)


if __name__ == "__main__":
    idade = safeIntegerInput("Digite sua idade: ")
    print("Sua idade é", idade)
