"""Projeto 07 — Perfil do Fibonacci memoizado.

Cada n relevante é efetivamente calculado uma vez; as demais consultas vêm do
dicionário. Assim, tempo e memória adicional são O(n).
"""
from time import perf_counter

def fib(n,memo,c):
    c[0]+=1
    if n in memo: return memo[n]
    memo[n]=1 if n<3 else fib(n-1,memo,c)+fib(n-2,memo,c)
    return memo[n]
for n in (10,100,500):
    c=[0]; inicio=perf_counter(); valor=fib(n,{},c); tempo=perf_counter()-inicio
    print(f"n={n} chamadas={c[0]} tempo={tempo:.8f}s dígitos={len(str(valor))}")
