"""Exemplo — função auxiliar aninhada para fatorial."""
def fatorial(n):
    def recursao(n,produto):
        if n==1: return produto
        return recursao(n-1,n*produto)
    return recursao(n,1)
print(fatorial(5))
