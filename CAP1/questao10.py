"""Capítulo 1 — Projeto 10: teste completo da classe ``Student``."""

try:
    from .EXEMPLOS.student import Student
except ImportError:
    from EXEMPLOS.student import Student


def main():
    aluno = Student("Ken Lambert", 3)
    aluno.setScore(0, 88)
    aluno.setScore(1, 77)
    aluno.setScore(2, 100)

    print(aluno)
    print("Quantidade de notas:", aluno.getNumberOfScores())
    print("Maior nota:", aluno.getHighScore())
    print("Média:", aluno.getAverage())
    print("Nome:", aluno.getName())
    print("Nota na posição 1:", aluno.getScore(1))


if __name__ == "__main__":
    main()
