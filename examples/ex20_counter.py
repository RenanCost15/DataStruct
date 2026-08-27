# Capítulo 1 — "Creating New Classes", classe Counter, p. 30–32.
# Correção necessária: self._value foi substituído por self.value em __str__.


class Counter(object):
    """Modela um contador."""

    # Variável de classe
    instances = 0

    # Construtor
    def __init__(self):
        """Configura o contador."""
        Counter.instances += 1
        self.reset()

    # Métodos mutadores
    def reset(self):
        """Define o contador como 0."""
        self.value = 0

    def increment(self, amount=1):
        """Adiciona uma quantidade ao contador."""
        self.value += amount

    def decrement(self, amount=1):
        """Subtrai uma quantidade do contador."""
        self.value -= amount

    # Métodos acessores
    def getValue(self):
        """Retorna o valor do contador."""
        return self.value

    def __str__(self):
        """Retorna a representação em string do contador."""
        return str(self.value)

    def __eq__(self, other):
        """Retorna True se self for igual a other; caso contrário, False."""
        if self is other:
            return True
        if type(self) != type(other):
            return False
        return self.value == other.value


c1 = Counter()
print(c1)
print(c1.getValue())
print(str(c1))
c1.increment()
print(c1)
c1.increment(5)
print(c1)
c1.reset()
print(c1)
c2 = Counter()
print(Counter.instances)
print(c1 == c1)
print(c1 == 0)
print(c1 == c2)
c2.increment()
print(c1 == c2)
