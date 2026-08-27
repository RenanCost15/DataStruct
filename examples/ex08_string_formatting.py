# Capítulo 1 — "Formatting Strings for Output", p. 14–15.

for exponent in range(7, 11):
    print(exponent, 10 ** exponent)

print("%6s" % "four")
print("%-6s" % "four")

for exponent in range(7, 11):
    print("%-3d%12d" % (exponent, 10 ** exponent))

salary = 100.00
print("Seu salário é $" + str(salary))
print("Seu salário é $%0.2f" % salary)
print("%6.3f" % 3.14)
