"""Exemplo — programa completo de adivinhação de número."""
import random

def main():
    menor=int(input("Digite o menor número: "))
    maior=int(input("Digite o maior número: "))
    numero=random.randint(menor,maior)
    tentativas=0
    while True:
        tentativas+=1
        palpite=int(input("Digite seu palpite: "))
        if palpite < numero: print("Muito pequeno")
        elif palpite > numero: print("Muito grande")
        else:
            print("Você acertou em",tentativas,"tentativas!"); break
if __name__=='__main__': main()
