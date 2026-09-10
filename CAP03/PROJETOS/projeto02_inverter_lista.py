"""Projeto 02 — Inverter uma lista sem usar list.reverse().
Complexidade: O(n) tempo e O(1) espaço adicional.
"""
def reverse(dados):
    esquerda,direita=0,len(dados)-1
    while esquerda<direita:
        dados[esquerda],dados[direita]=dados[direita],dados[esquerda]
        esquerda+=1; direita-=1

dados=[1,2,3,4,5]; reverse(dados); print(dados)
