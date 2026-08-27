# Capítulo 1 — Projects, questão 9, p. 35.

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
