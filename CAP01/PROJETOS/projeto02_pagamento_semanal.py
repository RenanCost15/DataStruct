"""Projeto 02 — calcular pagamento semanal incluindo horas extras a 1,5 vez o valor normal.

Resolução completa e comentada em PT-BR.
"""

# Capítulo 1 — Projeto 2, p. 33 do livro / p. 51 do PDF.

hourlyWage = float(input("Digite o salário por hora: "))
regularHours = float(input("Digite o total de horas regulares: "))
overtimeHours = float(input("Digite o total de horas extras: "))

weeklyPay = hourlyWage * regularHours
weeklyPay += overtimeHours * 1.5 * hourlyWage

print("Salário semanal total:", weeklyPay)
