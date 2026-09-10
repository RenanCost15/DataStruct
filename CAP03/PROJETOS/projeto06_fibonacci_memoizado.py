"""Projeto 06 — Fibonacci recursivo com memoização e contador de chamadas."""
class Contador:
    def __init__(self): self.valor=0
    def incrementar(self): self.valor+=1

def fib(n, memoria, contador):
    contador.incrementar()
    if n in memoria: return memoria[n]
    if n<3: valor=1
    else: valor=fib(n-1,memoria,contador)+fib(n-2,memoria,contador)
    memoria[n]=valor
    return valor

c=Contador(); print(fib(30,{},c)); print("Chamadas:",c.valor)
