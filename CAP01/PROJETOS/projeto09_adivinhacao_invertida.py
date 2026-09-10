"""Projeto 09 — inverter o jogo de adivinhação para o computador descobrir o número do usuário por busca binária.

Resolução completa e comentada em PT-BR.
"""

# Capítulo 1 — Projeto 9, p. 35 do livro / p. 53 do PDF.

from math import log2

smaller = int(input("Digite o menor número: "))
larger = int(input("Digite o maior número: "))
maximum = round(log2(larger - smaller) + 1)
count = 0

while True:
    count += 1
    guess = (smaller + larger) // 2
    print("Seu número é", guess)
    hint = input("Digite =, < ou >: ")

    if hint == "=":
        print("Oba, acertei em", count, "tentativas!")
        break
    elif hint == "<":
        larger = guess - 1
    elif hint == ">":
        smaller = guess + 1

    if count == maximum:
        print("Você está trapaceando!")
        break
