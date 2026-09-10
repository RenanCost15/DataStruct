"""Capítulo 3 — exemplo de comparação de objetos, p. 63 (PDF p. 81)."""
class SavingsAccount(object):
    """Representa uma conta poupança com nome, PIN e saldo."""
    def __init__(self, name, pin, balance=0.0):
        self.name = name
        self.pin = pin
        self.balance = balance
    def __lt__(self, other):
        return self.name < other.name
    def __eq__(self, other):
        return type(self) is type(other) and self.name == other.name and self.pin == other.pin and self.balance == other.balance

s1 = SavingsAccount("Ken", "1000", 0)
s2 = SavingsAccount("Bill", "1001", 30)
print(s1 < s2)
print(s2 < s1)
print(s1 > s2)
print(s2 > s1)
print(s2 == s1)
s3 = SavingsAccount("Ken", "1000", 0)
print(s1 == s3)
s4 = s1
print(s4 == s1)
