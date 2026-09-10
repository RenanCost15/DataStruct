"""Projeto 10 — modelar um estudante com nome e conjunto de notas, incluindo acesso, alteração e estatísticas.

Resolução completa e comentada em PT-BR.
"""

# Capítulo 1 — Projeto 10, p. 36 do livro / p. 54 do PDF.


class Student:
    def __init__(self, name, numberOfScores):
        self.name = name
        self.scores = [0] * numberOfScores

    def getName(self):
        return self.name

    def getScore(self, position):
        return self.scores[position]

    def setScore(self, position, score):
        self.scores[position] = score

    def getNumberOfScores(self):
        return len(self.scores)

    def getHighScore(self):
        return max(self.scores)

    def getAverageScore(self):
        return sum(self.scores) / len(self.scores)

    def __str__(self):
        result = "Nome: " + self.name + "\n"
        for index in range(len(self.scores)):
            result += "Nota " + str(index + 1) + ": " + str(self.scores[index]) + "\n"
        return result


def tester():
    student = Student("Ken Lambert", 3)
    student.setScore(0, 88)
    student.setScore(1, 77)
    student.setScore(2, 100)
    print(student)
    print("Nome:", student.getName())
    print("Nota na posição 0:", student.getScore(0))
    print("Número de notas:", student.getNumberOfScores())
    print("Maior nota:", student.getHighScore())
    print("Média:", student.getAverageScore())


if __name__ == "__main__":
    tester()
