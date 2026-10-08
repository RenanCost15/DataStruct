"""Joga com o usuário uma partida de adivinhar o número.

Exemplo do Capítulo 1 (arquivo ``numberguess.py``).
"""

import random


def main():
    """Lê os limites e repete os palpites até o acerto."""
    menor = int(input("Digite o menor número: "))
    maior = int(input("Digite o maior número: "))
    meu_numero = random.randint(menor, maior)
    tentativas = 0
    while True:
        tentativas += 1
        numero_usuario = int(input("Digite seu palpite: "))
        if numero_usuario < meu_numero:
            print("Muito pequeno")
        elif numero_usuario > meu_numero:
            print("Muito grande")
        else:
            print("Você acertou em", tentativas, "tentativas!")
            break


if __name__ == "__main__":
    main()
