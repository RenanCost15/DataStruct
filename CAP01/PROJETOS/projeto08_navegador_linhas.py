"""Projeto 08 — permitir navegação por número de linha em um arquivo-texto.

Resolução completa e comentada em PT-BR.
"""

# Capítulo 1 — Projeto 8, p. 35 do livro / p. 53 do PDF.

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
