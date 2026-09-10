"""Exercício 1.1 — Contar iterações de um laço que divide o problema por 2.

Resolução: a contagem cresce aproximadamente como floor(log2(n)) + 1 para n>0,
logo o laço é O(log n).
"""

def contar_iteracoes(tamanho):
    contador=0
    while tamanho > 0:
        tamanho//=2
        contador+=1
    return contador

if __name__ == "__main__":
    print(contar_iteracoes(1000))
