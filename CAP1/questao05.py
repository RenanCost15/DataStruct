"""Capítulo 1 — Projeto 5: cronograma do plano de crédito da TidBit."""

DOWN_PAYMENT_RATE = 0.10
ANNUAL_INTEREST_RATE = 0.12
MONTHLY_PAYMENT_RATE = 0.05


def cronograma_pagamentos(preco_compra):
    """Retorna as linhas do cronograma durante toda a vida do empréstimo."""
    if preco_compra <= 0:
        raise ValueError("O preço de compra deve ser positivo")

    entrada = preco_compra * DOWN_PAYMENT_RATE
    saldo = preco_compra - entrada
    pagamento_mensal = saldo * MONTHLY_PAYMENT_RATE
    linhas = []
    mes = 1

    while saldo > 0.005:
        saldo_atual = saldo
        juros = saldo_atual * ANNUAL_INTEREST_RATE / 12
        principal = pagamento_mensal - juros
        if principal > saldo_atual:
            principal = saldo_atual
        pagamento = principal + juros
        saldo = max(0.0, saldo_atual - principal)
        linhas.append((mes, saldo_atual, juros, principal, pagamento, saldo))
        mes += 1
    return entrada, pagamento_mensal, linhas


def main():
    preco = float(input("Preço de compra: "))
    entrada, pagamento_mensal, linhas = cronograma_pagamentos(preco)
    print(f"Entrada: {entrada:.2f}")
    print(f"Pagamento mensal previsto: {pagamento_mensal:.2f}\n")
    print(
        f"{'Mês':>4} {'Saldo atual':>13} {'Juros':>10} "
        f"{'Principal':>12} {'Pagamento':>12} {'Saldo restante':>16}"
    )
    for linha in linhas:
        mes, saldo, juros, principal, pagamento, restante = linha
        print(
            f"{mes:>4d} {saldo:>13.2f} {juros:>10.2f} "
            f"{principal:>12.2f} {pagamento:>12.2f} {restante:>16.2f}"
        )


if __name__ == "__main__":
    main()
