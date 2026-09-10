"""Projeto 04 — Exponenciação recursiva por divisão do expoente.
Complexidade O(log expoente) em tempo e pilha recursiva.
"""
def expo(numero, expoente):
    if expoente<0: raise ValueError("expoente deve ser não negativo")
    if expoente==0: return 1
    if expoente%2: return numero*expo(numero,expoente-1)
    metade=expo(numero,expoente//2)
    return metade*metade
print(expo(2,10))
