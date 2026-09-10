"""Projeto 08 — Complexidade de makeRandomList.

A operação `number in lista` é O(n) e é executada enquanto a lista cresce.
Sob as hipóteses simplificadoras do exercício, o custo típico é O(n²). Em sentido
probabilístico estrito, tentativas duplicadas acrescentam custo e não existe um
limite determinístico de tentativas para um gerador aleatório.
"""
import random

def makeRandomList(tamanho):
    dados=[]
    for _ in range(tamanho):
        while True:
            numero=random.randint(1,tamanho)
            if numero not in dados:
                dados.append(numero); break
    return dados
print(makeRandomList(10))
