"""Capítulo 3 — countfib.py, p. 54 (PDF p. 72).
Conta chamadas da função Fibonacci recursiva para tamanhos de problema que dobram.
A classe Counter foi desenvolvida no Capítulo 1.
"""
class Counter:
    """Mesma abstração Counter usada pelo livro para efetuar a contagem."""
    def __init__(self): self.value = 0
    def increment(self, amount=1): self.value += amount
    def __str__(self): return str(self.value)

def fib(n, counter):
    counter.increment()
    if n < 3:
        return 1
    return fib(n - 1, counter) + fib(n - 2, counter)

problemSize = 2
print("%12s%15s" % ("Tamanho", "Chamadas"))
for count in range(5):
    counter = Counter()
    fib(problemSize, counter)
    print("%12d%15s" % (problemSize, counter))
    problemSize *= 2
