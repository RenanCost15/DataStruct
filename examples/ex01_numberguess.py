# Capítulo 1 — "An Example Python Program: Guessing a Number", p. 2–3.

"""
Autor: Ken Lambert
Joga uma partida de adivinhação de número com o usuário.
"""

import random


def main():
    """Recebe os limites do intervalo e permite que o usuário tente
    adivinhar o número do computador até acertar."""
    smaller = int(input("Digite o menor número: "))
    larger = int(input("Digite o maior número: "))
    myNumber = random.randint(smaller, larger)
    count = 0
    while True:
        count += 1
        userNumber = int(input("Digite seu palpite: "))
        if userNumber < myNumber:
            print("Muito pequeno")
        elif userNumber > myNumber:
            print("Muito grande")
        else:
            print("Você acertou em", count, "tentativas!")
            break


if __name__ == "__main__":
    main()
