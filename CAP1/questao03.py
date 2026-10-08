"""Capítulo 1 — Projeto 3: distância percorrida por uma bola."""

BOUNCINESS_INDEX = 0.6


def distancia_total(altura_inicial, numero_de_quiques, indice=BOUNCINESS_INDEX):
    """Retorna a distância após a quantidade informada de quiques.

    Como no enunciado, o índice de elasticidade é 0,6. Cada quique contado
    termina no ponto mais alto; por isso, somente os anteriores incluem a
    descida correspondente.
    """
    if altura_inicial < 0 or numero_de_quiques < 0:
        raise ValueError("Altura e número de quiques não podem ser negativos")
    if not 0 <= indice <= 1:
        raise ValueError("O índice de elasticidade deve ficar entre 0 e 1")

    distancia = altura_inicial
    altura = altura_inicial
    for quique in range(numero_de_quiques):
        altura *= indice
        distancia += altura
        if quique < numero_de_quiques - 1:
            distancia += altura
    return distancia


def main():
    altura = float(input("Altura inicial da bola: "))
    quiques = int(input("Número de quiques: "))
    print(f"Distância total percorrida: {distancia_total(altura, quiques):.2f}")


if __name__ == "__main__":
    main()
