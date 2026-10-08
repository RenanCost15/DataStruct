"""Capítulo 1 — Projeto 7: teste do módulo ``stats.py``."""

try:
    from .stats import mean, median, mode
except ImportError:
    from stats import mean, median, mode


def main():
    dados = [10, 20, 20, 30, 40]
    print("Dados:", dados)
    print("Média:", mean(dados))
    print("Mediana:", median(dados))
    print("Moda:", mode(dados))


if __name__ == "__main__":
    main()
