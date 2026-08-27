# Capítulo 1 — Projects, questão 8, p. 35.

filename = input("Digite o nome do arquivo: ")
file = open(filename, "r")
lines = file.readlines()
file.close()

while True:
    print("Número de linhas no arquivo:", len(lines))
    lineNumber = int(input("Digite o número da linha (0 para sair): "))
    if lineNumber == 0:
        break
    print(lines[lineNumber - 1])
