# Capítulo 1 — Projects, questão 2, p. 33.

hourlyWage = float(input("Digite o salário por hora: "))
regularHours = float(input("Digite o total de horas regulares: "))
overtimeHours = float(input("Digite o total de horas extras: "))

weeklyPay = hourlyWage * regularHours
weeklyPay += overtimeHours * 1.5 * hourlyWage

print("Salário semanal total:", weeklyPay)
