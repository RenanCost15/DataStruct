"""Projeto 03 — Potência sem ** e sem pow.
Complexidade O(expoente) e espaço O(1) na versão iterativa.
"""
def expo(numero, expoente):
    if expoente<0: raise ValueError("expoente deve ser não negativo")
    resultado=1
    for _ in range(expoente): resultado*=numero
    return resultado
print(expo(2,10))
