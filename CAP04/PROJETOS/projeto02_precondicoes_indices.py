
class Array:
    def __init__(self,capacity,fillValue=None):
        self.initial=capacity; self.fill=fillValue; self.items=[fillValue]*capacity; self.logicalSize=0
    def __len__(self): return len(self.items)
    def size(self): return self.logicalSize
    def grow(self): self.items += [self.fill]*len(self.items)
    def shrink(self):
        new=max(self.initial,len(self.items)//2,self.logicalSize)
        self.items=self.items[:new]
    def append(self,x): self.insert(self.logicalSize,x)
    def insert(self,i,x):
        i=max(0,min(i,self.logicalSize))
        if self.logicalSize==len(self.items): self.grow()
        for k in range(self.logicalSize,i,-1): self.items[k]=self.items[k-1]
        self.items[i]=x; self.logicalSize+=1
    def pop(self,i=-1):
        if i==-1:i=self.logicalSize-1
        if not 0<=i<self.logicalSize: raise IndexError('índice fora do tamanho lógico')
        x=self.items[i]
        for k in range(i,self.logicalSize-1): self.items[k]=self.items[k+1]
        self.logicalSize-=1; self.items[self.logicalSize]=self.fill
        return x
    def __getitem__(self,i):
        if not 0<=i<self.logicalSize: raise IndexError('índice fora do tamanho lógico')
        return self.items[i]
    def __setitem__(self,i,x):
        if not 0<=i<self.logicalSize: raise IndexError('índice fora do tamanho lógico')
        self.items[i]=x
    def __iter__(self): return iter(self.items[:self.logicalSize])
    def __eq__(self,o): return type(self) is type(o) and self.logicalSize==o.logicalSize and list(self)==list(o)

"""Projeto 02 — Pré-condições de __getitem__/__setitem__."""
a=Array(3,0); a.append(10)
try: print(a[2])
except IndexError as erro: print("IndexError correto:",erro)
