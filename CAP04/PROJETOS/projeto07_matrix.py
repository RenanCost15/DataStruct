
class Grid:
    def __init__(self,rows,cols,fillValue=None): self.data=[[fillValue]*cols for _ in range(rows)]
    def getHeight(self): return len(self.data)
    def getWidth(self): return len(self.data[0])
    def __getitem__(self,i): return self.data[i]
    def __str__(self): return '\n'.join(' '.join(map(str,row)) for row in self.data)

"""Projeto 07 — Matrix estendendo Grid e usando operadores aritméticos."""
a=Matrix(2,2,0); b=Matrix(2,2,1)
a[0][0]=1; a[0][1]=2; a[1][0]=3; a[1][1]=4
print("A+B:\n", a+b, sep="")
