"""Capítulo 1 — Projeto 6: relatório da folha de pagamento."""


def carregar_folha(nome_arquivo):
    """Lê ``<sobrenome> <salário por hora> <horas trabalhadas>``."""
    registros = []
    with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
        for numero_linha, linha in enumerate(arquivo, start=1):
            if not linha.strip():
                continue
            campos = linha.split()
            if len(campos) != 3:
                raise ValueError(f"Formato inválido na linha {numero_linha}")
            sobrenome, salario_hora, horas = campos
            salario_hora = float(salario_hora)
            horas = float(horas)
            registros.append((sobrenome, horas, salario_hora * horas))
    return registros


def exibir_relatorio(registros):
    """Imprime nome, horas trabalhadas e salário do período."""
    print(f"{'Funcionário':<20}{'Horas':>12}{'Salário':>14}")
    for sobrenome, horas, salario in registros:
        print(f"{sobrenome:<20}{horas:>12.2f}{salario:>14.2f}")


def main():
    nome_arquivo = input("Nome do arquivo da folha de pagamento: ")
    exibir_relatorio(carregar_folha(nome_arquivo))


if __name__ == "__main__":
    main()
