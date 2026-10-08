"""Exercício 3.8 — Exibir um array 3D variando profundidade dentro de cada linha/coluna."""
a=[[[100*d+10*r+c for c in range(3)] for r in range(2)] for d in range(3)]
for r in range(2):
    for c in range(3):
        print(f"(linha={r}, coluna={c}):",*[a[d][r][c] for d in range(3)])
