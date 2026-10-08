
class Grid:
    def __init__(self,rows,cols,fillValue=None): self.data=[[fillValue]*cols for _ in range(rows)]
    def getHeight(self): return len(self.data)
    def getWidth(self): return len(self.data[0])
    def __getitem__(self,i): return self.data[i]
    def __str__(self): return '\n'.join(' '.join(map(str,row)) for row in self.data)

"""Exercício 3.4 — Conteúdo após matrix[row][column] = row * column.
Resultado:
0 0 0
0 1 2
0 2 4
"""
m=Grid(3,3,0)
for r in range(m.getHeight()):
    for c in range(m.getWidth()): m[r][c]=r*c
print(m)
