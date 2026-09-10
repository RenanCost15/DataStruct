"""Exercício 3.1 — Rastrear busca binária para 90 e 44."""

dados=[20,44,48,55,62,66,74,88,93,99]

def rastrear(alvo):
    esquerda, direita=0,len(dados)-1
    passos=[]
    while esquerda<=direita:
        meio=(esquerda+direita)//2
        passos.append((esquerda,direita,meio,dados[meio]))
        if dados[meio]==alvo: break
        if alvo < dados[meio]: direita=meio-1
        else: esquerda=meio+1
    return passos

for alvo in (90,44):
    print("Alvo",alvo)
    for p in rastrear(alvo): print("esq=%d dir=%d meio=%d valor=%d"%p)
