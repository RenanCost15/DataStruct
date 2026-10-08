"""Conta chamadas da função de Fibonacci para tamanhos que dobram."""

from pathlib import Path
import sys

# Mantém o ``from counter import Counter`` usado pelo livro e permite executar
# este arquivo isoladamente a partir de qualquer diretório.
COUNTER_DIRECTORY = Path(__file__).resolve().parents[2] / "CAP1" / "EXEMPLOS"
if str(COUNTER_DIRECTORY) not in sys.path:
    sys.path.insert(0, str(COUNTER_DIRECTORY))

from counter import Counter


def fib(n, counter):
    """Calcula Fibonacci e conta todas as chamadas da função."""
    counter.increment()
    if n < 3:
        return 1
    return fib(n - 1, counter) + fib(n - 2, counter)


def main():
    problem_size = 2
    print("%20s%15s" % ("Tamanho do problema", "Chamadas"))
    for _ in range(5):
        counter = Counter()
        fib(problem_size, counter)
        print("%20d%15s" % (problem_size, counter))
        problem_size *= 2


if __name__ == "__main__":
    main()
