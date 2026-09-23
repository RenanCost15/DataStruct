"""Capítulo 5 — testbag.py, p. 143 (PDF p. 161).
Programa de teste das implementações de bag; textos foram traduzidos para PT-BR.
"""
from pathlib import Path
import sys, importlib
p = Path(__file__).resolve().parent
sys.path.insert(0, str(p))
ArrayBag = importlib.import_module('05_arraybag').ArrayBag
LinkedBag = importlib.import_module('06_linkedbag').LinkedBag

def test(bagType):
    """Recebe um tipo de bag e executa os testes apresentados pelo livro."""
    print("Testando", bagType)
    lyst = [2013, 61, 1973]
    print("Lista de itens adicionados:", lyst)
    b1 = bagType(lyst)
    print("Tamanho, esperado 3:", len(b1))
    print("String da bag:", b1)
    print("2013 na bag, esperado True:", 2013 in b1)
    print("2012 na bag, esperado False:", 2012 in b1)
    print("Itens em linhas separadas:")
    for item in b1:
        print(item)
    b1.clear()
    print("Após limpar, esperado {}:", b1)
    b1.add(25)
    b1.remove(25)
    print("Após adicionar e remover 25, esperado {}:", b1)
    b1 = bagType(lyst)
    b2 = bagType(b1)
    print("Clonagem, esperado True para ==:", b1 == b2)
    print("Esperado False para is:", b1 is b2)
    print("Soma das duas bags, esperado dois de cada item:", b1 + b2)
    for item in lyst:
        b1.remove(item)
    print("Remover todos os itens, esperado {}:", b1)
    print("A remoção de item inexistente deve levantar KeyError:")
    # b2.remove(99)  # descomente para reproduzir o encerramento com KeyError.

test(ArrayBag)
# test(LinkedBag)  # o livro deixa esta chamada comentada para alternar implementações.
