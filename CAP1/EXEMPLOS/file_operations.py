"""Operações com arquivos de texto e objetos mostradas no Capítulo 1."""

from pathlib import Path
import pickle
import random


def write_text(path):
    """Grava as duas linhas do exemplo em ``path``."""
    with open(path, "w", encoding="utf-8") as file_obj:
        file_obj.write("Primeira linha.\nSegunda linha.\n")


def read_text(path):
    """Retorna todo o conteúdo textual de ``path``."""
    with open(path, "r", encoding="utf-8") as file_obj:
        return file_obj.read()


def write_random_integers(path, quantity=500, seed=None):
    """Grava inteiros aleatórios entre 1 e 500, um por linha."""
    generator = random.Random(seed)
    with open(path, "w", encoding="utf-8") as file_obj:
        for _ in range(quantity):
            number = generator.randint(1, 500)
            file_obj.write(str(number) + "\n")


def sum_integers(path):
    """Lê inteiros separados por espaços ou linhas e retorna a soma."""
    with open(path, "r", encoding="utf-8") as file_obj:
        return sum(map(int, file_obj.read().split()))


def save_objects(path, items):
    """Serializa individualmente os objetos de ``items``."""
    with open(path, "wb") as file_obj:
        for item in items:
            pickle.dump(item, file_obj)


def load_objects(path):
    """Carrega objetos serializados até encontrar o fim do arquivo."""
    items = []
    with open(path, "rb") as file_obj:
        while True:
            try:
                items.append(pickle.load(file_obj))
            except EOFError:
                break
    return items


def main():
    base = Path(__file__).resolve().parent
    text_path = base / "myfile.txt"
    integers_path = base / "integers.txt"
    objects_path = base / "items.dat"

    write_text(text_path)
    print(read_text(text_path), end="")

    write_random_integers(integers_path, seed=1)
    print("A soma é", sum_integers(integers_path))

    original = [60, "Um objeto string", 1977]
    save_objects(objects_path, original)
    print(load_objects(objects_path))


if __name__ == "__main__":
    main()
