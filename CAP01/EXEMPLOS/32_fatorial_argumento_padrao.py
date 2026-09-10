"""Exemplo — fatorial recursivo com acumulador como argumento padrão."""
def fatorial(n,produto=1):
    if n==1: return produto
    return fatorial(n-1,n*produto)
print(fatorial(5))
