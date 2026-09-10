"""Exemplo — classe Counter com variável de classe, mutadores, acessores e operadores."""
class Counter:
    instances=0
    def __init__(self):
        Counter.instances+=1; self.reset()
    def reset(self): self.value=0
    def increment(self,amount=1): self.value+=amount
    def decrement(self,amount=1): self.value-=amount
    def getValue(self): return self.value
    def __str__(self): return str(self.value)
    def __eq__(self,other): return type(self) is type(other) and self.value==other.value
c1=Counter(); c2=Counter(); c1.increment(5); print(c1,c1==c2,Counter.instances)
