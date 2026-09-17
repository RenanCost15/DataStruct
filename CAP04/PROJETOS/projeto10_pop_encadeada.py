
class Node:
    def __init__(self,data,next=None): self.data=data; self.next=next
class TwoWayNode(Node):
    def __init__(self,data,previous=None,next=None): super().__init__(data,next); self.previous=previous
def comprimento_encadeado(head):
    n=0; p=head
    while p is not None: n+=1; p=p.next
    return n
def inserir_encadeado(item,posicao,head):
    if head is None or posicao<=0:return Node(item,head)
    p=head
    while posicao>1 and p.next is not None: p=p.next; posicao-=1
    p.next=Node(item,p.next); return head
def remover_encadeado(posicao,head):
    if head is None or posicao<0 or posicao>=comprimento_encadeado(head):raise IndexError
    if posicao==0:return head.next,head.data
    p=head
    for _ in range(posicao-1):p=p.next
    x=p.next; p.next=x.next; return head,x.data
def tornar_duplamente_encadeada(head):
    newhead=tail=None; p=head
    while p is not None:
        n=TwoWayNode(p.data,tail)
        if tail is None:newhead=n
        else:tail.next=n
        tail=n;p=p.next
    return newhead

"""Projeto 10 — Remover e retornar item de posição encadeada."""
head=Node(1,Node(2,Node(3))); head,item=remover_encadeado(1,head)
print("removido",item)
