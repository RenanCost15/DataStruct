
class ArrayBag:
    DEFAULT_CAPACITY=10
    def __init__(self,sourceCollection=None):
        self.items=[None]*self.DEFAULT_CAPACITY; self.size=0; self.modCount=0
        if sourceCollection:
            for x in sourceCollection:self.add(x)
    def __len__(self):return self.size
    def isEmpty(self):return self.size==0
    def _grow(self):self.items += [None]*len(self.items)
    def add(self,x):
        if self.size==len(self.items):self._grow()
        self.items[self.size]=x;self.size+=1;self.modCount+=1
    def __iter__(self):
        expected=self.modCount
        for i in range(self.size):
            yield self.items[i]
            if expected!=self.modCount:raise RuntimeError('coleção alterada durante a iteração')
    def count(self,x):return sum(1 for y in self if x==y)
    def __contains__(self,x):return any(x==y for y in self)
    def __eq__(self,o):return type(self) is type(o) and len(self)==len(o) and all(self.count(x)==o.count(x) for x in self)
    def __add__(self,o):
        r=type(self)(self)
        for x in o:r.add(x)
        return r
    def clone(self):return type(self)(self)
    def remove(self,x):
        idx=-1
        for i,y in enumerate(self):
            if y==x:idx=i;break
        if idx<0:raise KeyError(x)
        for i in range(idx,self.size-1):self.items[i]=self.items[i+1]
        self.size-=1;self.items[self.size]=None;self.modCount+=1
class Node:
    def __init__(self,data,next=None):self.data=data;self.next=next
class LinkedBag(ArrayBag):
    def __init__(self,sourceCollection=None):
        self.items=None;self.size=0;self.modCount=0
        if sourceCollection:
            for x in sourceCollection:self.add(x)
    def add(self,x):self.items=Node(x,self.items);self.size+=1;self.modCount+=1
    def __iter__(self):
        p=self.items;expected=self.modCount
        while p is not None:
            yield p.data
            if expected!=self.modCount:raise RuntimeError('coleção alterada durante a iteração')
            p=p.next
    def remove(self,x):
        p=self.items;t=None
        while p and p.data!=x:t=p;p=p.next
        if p is None:raise KeyError(x)
        if t is None:self.items=p.next
        else:t.next=p.next
        self.size-=1;self.modCount+=1
class ArraySet(ArrayBag):
    def add(self,x):
        if x not in self:super().add(x)
class LinkedSet(LinkedBag):
    def add(self,x):
        if x not in self:super().add(x)
class ArraySortedBag(ArrayBag):
    def add(self,x):
        if self.size==len(self.items):self._grow()
        i=0
        while i<self.size and self.items[i]<=x:i+=1
        for k in range(self.size,i,-1):self.items[k]=self.items[k-1]
        self.items[i]=x;self.size+=1;self.modCount+=1
    def __contains__(self,x):
        l=0;r=self.size-1
        while l<=r:
            m=(l+r)//2
            if self.items[m]==x:return True
            if x<self.items[m]:r=m-1
            else:l=m+1
        return False

"""Projeto 07 — LinkedSet: conjunto baseado em nós, sem duplicatas."""
s=LinkedSet([1,1,2,3]); s.add(2); s.add(4)
print(list(s),"tamanho",len(s))
assert set(s)=={1,2,3,4}
