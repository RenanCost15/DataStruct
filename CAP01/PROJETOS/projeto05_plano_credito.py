"""Projeto 05 — gerar a tabela mensal de um plano de crédito com entrada, juros, principal e saldo.

Resolução completa e comentada em PT-BR.
"""

# Capítulo 1 — Projeto 5, p. 34 do livro / p. 52 do PDF.

ANNUAL_RATE = 0.12
MONTHLY_RATE = ANNUAL_RATE / 12

purchasePrice = float(input("Digite o preço da compra: "))
downPayment = purchasePrice * 0.10
balance = purchasePrice - downPayment
monthlyPayment = balance * 0.05
month = 1

print("Mês  Saldo atual  Juros  Principal  Pagamento  Saldo restante")

while balance > 0:
    interest = balance * MONTHLY_RATE
    payment = monthlyPayment
    if payment > balance + interest:
        payment = balance + interest
    principal = payment - interest
    remainingBalance = balance - principal

    print("%3d  %11.2f  %5.2f  %9.2f  %9.2f  %15.2f" %
          (month, balance, interest, principal, payment, remainingBalance))

    balance = remainingBalance
    month += 1
