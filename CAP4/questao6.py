"""Capítulo 4 — Projeto 6: remoção de __iter__ e ajuste de __str__.

Remover ``__iter__`` é uma boa sugestão porque um objeto que implementa
``__getitem__`` com índices consecutivos já pode ser percorrido pelo protocolo
de sequência de Python. A iteração solicita as posições 0, 1, 2, ... e termina
quando ``__getitem__`` lança ``IndexError``. Como a pré-condição desse método
agora usa o tamanho lógico, somente os itens logicamente presentes aparecem.

``__str__`` não deve mais converter diretamente ``self.items``, pois isso
mostraria também as células livres da capacidade física. Ele deve montar a
representação a partir das posições de 0 até ``size() - 1``; por exemplo:

    def __str__(self):
        return str([self[index] for index in range(self.size())])
"""


if __name__ == "__main__":
    print(__doc__)
