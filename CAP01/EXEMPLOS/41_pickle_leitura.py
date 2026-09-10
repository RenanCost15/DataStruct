"""Exemplo — ler objetos pickle até EOFError."""
import pickle
with open('itens.dat','wb') as f:
    for item in [60,'Uma string',1977]: pickle.dump(item,f)
itens=[]
with open('itens.dat','rb') as f:
    while True:
        try: itens.append(pickle.load(f))
        except EOFError: break
print(itens)
