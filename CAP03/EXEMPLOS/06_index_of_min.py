"""Capítulo 3 — função indexOfMin, p. 59 (PDF p. 77)."""
def indexOfMin(lyst):
    """Retorna o índice do menor item."""
    minIndex = 0
    currentIndex = 1
    while currentIndex < len(lyst):
        if lyst[currentIndex] < lyst[minIndex]:
            minIndex = currentIndex
        currentIndex += 1
    return minIndex
