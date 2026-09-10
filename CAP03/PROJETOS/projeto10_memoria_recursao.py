"""Projeto 10 — Complexidade espacial de fatorial e Fibonacci recursivos.

Fatorial recursivo: profundidade máxima n -> O(n) memória de pilha.
Fibonacci recursivo ingênuo: embora execute exponencialmente muitas chamadas,
apenas uma cadeia de profundidade O(n) fica ativa por vez -> O(n) memória de pilha.
"""
ANALISE={"fatorial":"O(n)","fibonacci_recursivo":"O(n) memória simultânea; tempo exponencial"}
print(ANALISE)
