# Capítulo 1 — Projects, questão 6, p. 34–35.

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
