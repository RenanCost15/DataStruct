"""Exercício 2.2 — Comparar A=n² e B=(n²+n)/2.

A-B=(n²-n)/2=n(n-1)/2. Para n>1, A faz mais trabalho. Em n=0 ou n=1,
os valores coincidem. Quando n cresce, B tende a aproximadamente metade do
trabalho de A, mas ambos continuam O(n²): a diferença é de constante, não de ordem.
"""
for n in (1,2,10,100):
    a=n*n; b=(n*n+n)//2
    print(n,a,b)
