"""Exemplo — leitura linha a linha com readline e sentinela string vazia."""
with open('meuarquivo.txt','w',encoding='utf-8') as f: f.write('A\nB\n')
f=open('meuarquivo.txt','r',encoding='utf-8')
while True:
    linha=f.readline()
    if linha=='': break
    print(linha,end='')
f.close()
