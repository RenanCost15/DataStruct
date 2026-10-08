"""Capítulo 1 — Projeto 9: o computador adivinha o número."""

import math


def maximo_de_tentativas(menor, maior):
    """Aplica o limite ``round(log2(maior - menor) + 1)`` do livro."""
    if menor > maior:
        raise ValueError("O limite inferior deve ser menor ou igual ao superior")
    if menor == maior:
        return 1
    return round(math.log2(maior - menor) + 1)


def main():
    menor = int(input("Digite o menor número: "))
    maior = int(input("Digite o maior número: "))
    limite = maximo_de_tentativas(menor, maior)
    tentativas = 0

    while menor <= maior:
        palpite = (menor + maior) // 2
        tentativas += 1
        print("Seu número é", palpite)
        dica = input("Digite =, < ou >: ").strip()

        if dica == "=":
            print(f"Oba, acertei em {tentativas} tentativas!")
            return
        if dica == "<":
            maior = palpite - 1
        elif dica == ">":
            menor = palpite + 1
        else:
            print("Dica inválida. Use somente =, < ou >.")
            tentativas -= 1
            continue

        if tentativas >= limite or menor > maior:
            print("Você está trapaceando!")
            return


if __name__ == "__main__":
    main()
