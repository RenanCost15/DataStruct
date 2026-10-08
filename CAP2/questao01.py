"""Capítulo 2 — Projeto 1: exploração das coleções embutidas.

O enunciado pede o uso de ``dir(<tipo>)`` e ``help(<tipo>)`` para ``str``,
``list``, ``tuple``, ``set`` e ``dict``. Este programa faz exatamente essas
chamadas para os cinco tipos.
"""

COLLECTION_TYPES = (str, list, tuple, set, dict)


def nomes_da_interface(collection_type):
    """Retorna os atributos e métodos expostos pelo tipo."""
    return dir(collection_type)


def main():
    for collection_type in COLLECTION_TYPES:
        print("\n" + "=" * 72)
        print("TIPO:", collection_type.__name__)
        print("dir:")
        print(nomes_da_interface(collection_type))
        print("\nhelp:")
        help(collection_type)


if __name__ == "__main__":
    main()
