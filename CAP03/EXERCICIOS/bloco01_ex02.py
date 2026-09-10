"""Exercício 1.2 — Executar o contador para vários tamanhos.

Conclusão: dobrar n acrescenta aproximadamente 1 iteração; multiplicar n por
10 acrescenta aproximadamente log2(10) ~= 3,32 iterações. Isso caracteriza
crescimento logarítmico.
"""

def contar(n):
    c=0
    while n>0:
        n//=2; c+=1
    return c

if __name__ == "__main__":
    for n in (1000,2000,4000,10000,100000):
        print(n, contar(n))
