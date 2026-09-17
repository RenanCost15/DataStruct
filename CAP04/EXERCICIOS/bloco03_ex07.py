"""Exercício 3.7 — Inicializar cada célula 3D com o número de seus índices."""
profundidade,linhas,colunas=3,4,4
a=[[[0 for _ in range(colunas)] for _ in range(linhas)] for _ in range(profundidade)]
for d in range(profundidade):
    for r in range(linhas):
        for c in range(colunas): a[d][r][c]=100*d+10*r+c
print(a[2][3][3])  # 233
