
class AbstractCollection:
    def __init__(self,sourceCollection=None):
        self.size=0
        if sourceCollection:
            for x in sourceCollection:self.add(x)
    def __len__(self):return self.size
    def isEmpty(self):return len(self)==0
    def count(self,x):return sum(1 for y in self if y==x)
    def __add__(self,o):
        r=type(self)(self)
        for x in o:r.add(x)
        return r
    def clone(self):return type(self)(self)
    def __eq__(self,o):
        if self is o:return True
        if type(self)!=type(o) or len(self)!=len(o):return False
        it=iter(o)
        return all(x==next(it) for x in self)
class AbstractBag(AbstractCollection):
    def __eq__(self,o):return type(self)==type(o) and len(self)==len(o) and all(self.count(x)==o.count(x) for x in self)
class ArrayBag(AbstractBag):
    def __init__(self,sourceCollection=None):
        self.items=[None]*10;self.position=-1;super().__init__(sourceCollection)
    def __iter__(self):return iter(self.items[:self.size])
    def add(self,x):
        if self.size==len(self.items):self.items += [None]*len(self.items)
        self.items[self.size]=x;self.size+=1
    def __contains__(self,x):
        self.position=-1
        for i,y in enumerate(self):
            if x==y:self.position=i;return True
        return False
    def remove(self,x):
        if x not in self:raise KeyError(x)
        for i in range(self.position,self.size-1):self.items[i]=self.items[i+1]
        self.size-=1;self.items[self.size]=None;self.position=-1
class Node:
    def __init__(self,data,next=None):self.data=data;self.next=next
class LinkedBag(AbstractBag):
    def __init__(self,sourceCollection=None):self.items=None;self._found=None;self._trailer=None;super().__init__(sourceCollection)
    def __iter__(self):
        p=self.items
        while p:yield p.data;p=p.next
    def add(self,x):self.items=Node(x,self.items);self.size+=1
    def __contains__(self,x):
        p=self.items;t=None
        while p and p.data!=x:t=p;p=p.next
        self._found=p;self._trailer=t;return p is not None
    def remove(self,x):
        if x not in self:raise KeyError(x)
        if self._trailer is None:self.items=self._found.next
        else:self._trailer.next=self._found.next
        self.size-=1;self._found=self._trailer=None
class ArraySortedBag(ArrayBag):
    def add(self,x):
        if self.size==len(self.items):self.items += [None]*len(self.items)
        i=0
        while i<self.size and self.items[i]<=x:i+=1
        for k in range(self.size,i,-1):self.items[k]=self.items[k-1]
        self.items[i]=x;self.size+=1
    def __contains__(self,x):
        l=0;r=self.size-1;self.position=-1
        while l<=r:
            m=(l+r)//2
            if self.items[m]==x:self.position=m;return True
            if x<self.items[m]:r=m-1
            else:l=m+1
        return False
class ArraySet(ArrayBag):
    def add(self,x):
        if x not in self:super().add(x)
class LinkedSet(LinkedBag):
    def add(self,x):
        if x not in self:super().add(x)
class ArraySortedSet(ArraySortedBag):
    def add(self,x):
        if x not in self:super().add(x)

"""Projeto 08 — Evitar a segunda busca em ArrayBag.remove.
A biblioteca mantém a posição encontrada por __contains__ e remove usa essa
informação para fechar o buraco sem repetir a busca.
"""
b=ArrayBag([10,20,30,40]); print(30 in b); b.remove(30); print(list(b))
