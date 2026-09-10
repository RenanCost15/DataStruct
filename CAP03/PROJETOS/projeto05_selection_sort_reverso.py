"""Capítulo 3 — Projeto 5 (p. 87 / PDF p. 105).
Enunciado em PT-BR: acrescente a selectionSort um argumento keyword `reverse`, padrão False, para permitir ordenação decrescente.
"""
def selectionSort(lyst, reverse=False):
    i=0
    while i<len(lyst)-1:
        chosen=i; j=i+1
        while j<len(lyst):
            if (lyst[j] > lyst[chosen]) if reverse else (lyst[j] < lyst[chosen]): chosen=j
            j+=1
        if chosen!=i: lyst[i],lyst[chosen]=lyst[chosen],lyst[i]
        i+=1
if __name__=='__main__':
    for reverse in (False,True):
        dados=[5,1,4,2,3]; selectionSort(dados,reverse); print(reverse,dados)
