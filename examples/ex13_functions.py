# Capítulo 1 — "Creating New Functions", p. 19–20.


def square(n):
    """Retorna o quadrado de n."""
    result = n ** 2
    return result


print(square(5))

# O livro mostra que esta chamada, nesta posição, gera NameError.
# first()


def first():
    print("Chamando first.")
    second()


def second():
    print("Chamando second.")


first()
