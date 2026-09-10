"""Exercício 1.3 — Medir tempo de CPU em vez de tempo de parede.

Resolução: time.process_time() (ou process_time_ns()) mede o tempo de CPU usado
pelo processo e não conta, por exemplo, o tempo em que o programa fica dormindo.
Isso é mais adequado quando se quer isolar processamento do tempo decorrido.
"""
from time import process_time
inicio=process_time()
soma=sum(range(1_000_000))
fim=process_time()
print("Tempo de CPU:", fim-inicio, "resultado:", soma)
