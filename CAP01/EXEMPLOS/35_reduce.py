"""Exemplo — reduce acumula itens em um único valor."""
from functools import reduce
print(reduce(lambda x,y:x*y,range(1,11)))
