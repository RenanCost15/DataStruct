"""Projeto 06 — Por que um Array semelhante a list deve iterar só pelo tamanho lógico?

A iteração não pode expor células de capacidade ainda não ocupadas. Portanto,
__iter__ deve percorrer 0..logicalSize-1; __str__ deve se basear no mesmo percurso,
e não em toda a área física de armazenamento. A implementação auxiliar do
repositório já segue esse contrato.
"""
print(__doc__)
