"""Capítulo 1 — Projeto 1: medidas de uma esfera."""

import math


def medidas_esfera(raio):
    """Retorna diâmetro, circunferência, área e volume da esfera."""
    if raio < 0:
        raise ValueError("O raio não pode ser negativo")
    diametro = 2 * raio
    circunferencia = 2 * math.pi * raio
    area_superficie = 4 * math.pi * raio ** 2
    volume = (4 / 3) * math.pi * raio ** 3
    return diametro, circunferencia, area_superficie, volume


def main():
    raio = float(input("Digite o raio da esfera: "))
    diametro, circunferencia, area, volume = medidas_esfera(raio)
    print(f"Diâmetro: {diametro:.2f}")
    print(f"Circunferência: {circunferencia:.2f}")
    print(f"Área da superfície: {area:.2f}")
    print(f"Volume: {volume:.2f}")


if __name__ == "__main__":
    main()
