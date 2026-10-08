"""Capítulo 4 — Projeto 7: classe Matrix derivada de Grid."""


class Grid:
    def __init__(self, rows, columns, fillValue=None):
        self.data = [[fillValue for _ in range(columns)] for _ in range(rows)]

    def getHeight(self):
        return len(self.data)

    def getWidth(self):
        return len(self.data[0]) if self.data else 0

    def __getitem__(self, row):
        return self.data[row]

    def __str__(self):
        return "\n".join(" ".join(map(str, row)) for row in self.data)


class Matrix(Grid):
    """Matriz com adição, subtração e multiplicação por matriz ou escalar."""

    def _sameShape(self, other):
        return (isinstance(other, Matrix)
                and self.getHeight() == other.getHeight()
                and self.getWidth() == other.getWidth())

    def _elementwise(self, other, operation):
        if not self._sameShape(other):
            raise ValueError("as matrizes devem ter as mesmas dimensões")
        result = Matrix(self.getHeight(), self.getWidth(), 0)
        for row in range(self.getHeight()):
            for column in range(self.getWidth()):
                result[row][column] = operation(self[row][column],
                                                other[row][column])
        return result

    def __add__(self, other):
        return self._elementwise(other, lambda left, right: left + right)

    def __sub__(self, other):
        return self._elementwise(other, lambda left, right: left - right)

    def __mul__(self, other):
        if isinstance(other, Matrix):
            if self.getWidth() != other.getHeight():
                raise ValueError("dimensões incompatíveis para multiplicação")
            result = Matrix(self.getHeight(), other.getWidth(), 0)
            for row in range(self.getHeight()):
                for column in range(other.getWidth()):
                    result[row][column] = sum(
                        self[row][index] * other[index][column]
                        for index in range(self.getWidth())
                    )
            return result
        result = Matrix(self.getHeight(), self.getWidth(), 0)
        for row in range(self.getHeight()):
            for column in range(self.getWidth()):
                result[row][column] = self[row][column] * other
        return result

    def __rmul__(self, scalar):
        return self * scalar


if __name__ == "__main__":
    first = Matrix(2, 2, 0)
    second = Matrix(2, 2, 0)
    first[0][:], first[1][:] = [1, 2], [3, 4]
    second[0][:], second[1][:] = [5, 6], [7, 8]
    print("A + B:\n" + str(first + second))
    print("A - B:\n" + str(first - second))
    print("A * B:\n" + str(first * second))
    print("2 * A:\n" + str(2 * first))
