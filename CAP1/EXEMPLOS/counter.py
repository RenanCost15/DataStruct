"""Definição da classe ``Counter`` apresentada no Capítulo 1."""


class Counter(object):
    """Modela um contador inteiro."""

    instances = 0

    def __init__(self):
        """Configura o contador."""
        Counter.instances += 1
        self.reset()

    def reset(self):
        """Define o contador como 0."""
        self.value = 0

    def increment(self, amount=1):
        """Adiciona ``amount`` ao contador."""
        self.value += amount

    def decrement(self, amount=1):
        """Subtrai ``amount`` do contador."""
        self.value -= amount

    def getValue(self):
        """Retorna o valor do contador."""
        return self.value

    def __str__(self):
        """Retorna a representação textual do contador."""
        return str(self.value)

    def __eq__(self, other):
        """Retorna ``True`` quando dois contadores têm o mesmo valor."""
        if self is other:
            return True
        if type(self) is not type(other):
            return False
        return self.value == other.value
