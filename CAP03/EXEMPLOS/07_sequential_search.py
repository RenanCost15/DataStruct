"""Capítulo 3 — função sequentialSearch, p. 60 (PDF p. 78)."""
def sequentialSearch(target, lyst):
    """Retorna a posição do alvo se encontrado; caso contrário, -1."""
    position = 0
    while position < len(lyst):
        if target == lyst[position]:
            return position
        position += 1
    return -1
