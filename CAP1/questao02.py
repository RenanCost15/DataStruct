"""Capítulo 1 — Projeto 2: salário semanal."""


def salario_semanal(salario_hora, horas_regulares, horas_extras):
    """Calcula o pagamento regular mais horas extras a 1,5 vez a tarifa."""
    if min(salario_hora, horas_regulares, horas_extras) < 0:
        raise ValueError("Os valores informados não podem ser negativos")
    pagamento_regular = salario_hora * horas_regulares
    pagamento_extra = horas_extras * 1.5 * salario_hora
    return pagamento_regular + pagamento_extra


def main():
    salario_hora = float(input("Salário por hora: "))
    horas_regulares = float(input("Total de horas regulares: "))
    horas_extras = float(input("Total de horas extras: "))
    total = salario_semanal(salario_hora, horas_regulares, horas_extras)
    print(f"Salário semanal total: R$ {total:.2f}")


if __name__ == "__main__":
    main()
