"""Exemplo — converter texto de arquivo para inteiros antes de somar."""
with open('inteiros.txt','w',encoding='utf-8') as f: f.write('10\n20\n30\n')
with open('inteiros.txt','r',encoding='utf-8') as f:
    total=sum(map(int,f.read().split()))
print('A soma é',total)
