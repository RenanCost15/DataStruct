"""Exemplo — escrever e ler arquivo de texto."""
with open('meuarquivo.txt','w',encoding='utf-8') as f: f.write('Primeira linha.\nSegunda linha.\n')
with open('meuarquivo.txt','r',encoding='utf-8') as f: print(f.read())
