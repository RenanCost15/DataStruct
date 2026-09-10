"""Projeto 06 — ler arquivo de funcionários e produzir relatório tabular de salários do período.

Resolução completa e comentada em PT-BR.
"""

# Capítulo 1 — Projeto 6, p. 34-35 do livro / p. 52-53 do PDF.

filename = input("Digite o nome do arquivo: ")
file = open(filename, "r")

print("Funcionário       Horas trabalhadas       Salário pago")
for line in file:
    lastName, hourlyWage, hoursWorked = line.split()
    hourlyWage = float(hourlyWage)
    hoursWorked = float(hoursWorked)
    wagesPaid = hourlyWage * hoursWorked
    print("%-18s%17.2f%19.2f" % (lastName, hoursWorked, wagesPaid))

file.close()
