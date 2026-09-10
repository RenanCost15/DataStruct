"""Exemplo — descobrir componentes e documentação em tempo de execução."""
import math
print("Alguns membros de math:", [n for n in dir(math) if not n.startswith('_')][:10])
print(abs.__doc__)
