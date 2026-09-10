"""Capítulo 3 — Projeto 9 (p. 88 / PDF p. 106).
Enunciado em PT-BR: faça quicksort chamar insertion sort para sublistas menores que 50 itens; compare com o original em 50, 500 e 5000 itens e ajuste o limiar para procurar uma configuração melhor.
"""
import random, time

def insertion_range(a,l,r):
    for i in range(l+1,r+1):
        x=a[i]; j=i-1
        while j>=l and x<a[j]: a[j+1]=a[j]; j-=1
        a[j+1]=x

def quicksort(a,threshold=0):
    def q(l,r):
        if l>=r:return
        if threshold and r-l+1<threshold: insertion_range(a,l,r); return
        m=(l+r)//2; a[m],a[r]=a[r],a[m]; pivot=a[r]; b=l
        for i in range(l,r):
            if a[i]<pivot: a[i],a[b]=a[b],a[i]; b+=1
        a[b],a[r]=a[r],a[b]
        q(l,b-1); q(b+1,r)
    q(0,len(a)-1)

def medir(n,threshold):
    dados=list(range(n)); random.shuffle(dados); t=time.perf_counter(); quicksort(dados,threshold); return time.perf_counter()-t
if __name__=='__main__':
    for n in (50,500,5000):
        print(n,'original',medir(n,0),'limiar50',medir(n,50))
    for limiar in (10,20,30,40,50,60,80): print('limiar',limiar,'t=',medir(5000,limiar))
