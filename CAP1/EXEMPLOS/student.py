"""Classe ``Student`` solicitada no Projeto 10 do Capítulo 1."""


class Student(object):
    """Mantém o nome de um aluno e suas notas de teste."""

    def __init__(self, name, number_of_scores):
        if number_of_scores < 0:
            raise ValueError("A quantidade de notas não pode ser negativa")
        self._name = name
        self._scores = [0] * number_of_scores

    def getName(self):
        """Retorna o nome do aluno."""
        return self._name

    def getScore(self, position):
        """Retorna a nota na posição informada, contando a partir de 0."""
        return self._scores[position]

    def setScore(self, position, score):
        """Substitui a nota na posição informada."""
        self._scores[position] = score

    def getNumberOfScores(self):
        """Retorna a quantidade de notas."""
        return len(self._scores)

    def getHighScore(self):
        """Retorna a maior nota, ou 0 quando não existem notas."""
        return max(self._scores, default=0)

    def getAverage(self):
        """Retorna a média das notas, ou 0 quando não existem notas."""
        if not self._scores:
            return 0
        return sum(self._scores) / len(self._scores)

    def __str__(self):
        lines = ["Name: " + self._name]
        for position, score in enumerate(self._scores, start=1):
            lines.append(f"Score {position}: {score}")
        return "\n".join(lines)
