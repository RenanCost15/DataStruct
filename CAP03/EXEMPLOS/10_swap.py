"""Capítulo 3 — função swap, p. 64 (PDF p. 82)."""
def swap(lyst, i, j):
    """Troca os itens das posições i e j."""
    temp = lyst[i]
    lyst[i] = lyst[j]
    lyst[j] = temp
