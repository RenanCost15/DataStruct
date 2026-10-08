
class Grid:
    def __init__(self,rows,cols,fillValue=None): self.data=[[fillValue]*cols for _ in range(rows)]
    def getHeight(self): return len(self.data)
    def getWidth(self): return len(self.data[0])
    def __getitem__(self,i): return self.data[i]
    def __str__(self): return '\n'.join(' '.join(map(str,row)) for row in self.data)

"""Exercício 3.3 — Encontrar o primeiro inteiro negativo em Grid."""
g=Grid(3,4,1); g[1][2]=-7
row,column=g.getHeight(),g.getWidth()
achou=False
for r in range(g.getHeight()):
    for c in range(g.getWidth()):
        if g[r][c] < 0:
            row,column=r,c; achou=True; break
    if achou: break
print(row,column)
