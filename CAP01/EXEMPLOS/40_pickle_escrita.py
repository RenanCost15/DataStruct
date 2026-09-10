"""Exemplo — serializar vários objetos com pickle."""
import pickle
itens=[60,'Uma string',1977]
with open('itens.dat','wb') as f:
    for item in itens: pickle.dump(item,f)
print('gravado')
