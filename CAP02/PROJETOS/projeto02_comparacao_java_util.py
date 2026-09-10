"""Projeto 02 — Comparação conceitual com java.util.

Enunciado em PT-BR:
Compare as coleções Python com as coleções da biblioteca java.util.

Resolução resumida e comentada:
- list: Python list combina várias capacidades que em Java aparecem em
  ArrayList/LinkedList; Java usa tipagem genérica declarada.
- tuple: Java SE tradicional não possui uma tupla geral equivalente no núcleo.
- set: set aproxima-se de HashSet; TreeSet mantém ordenação natural.
- dict: dict corresponde conceitualmente a Map, como HashMap; TreeMap mantém
  chaves ordenadas.
- iteração: Python usa __iter__/__next__; Java usa Iterable/Iterator e for-each.
"""

COMPARACAO = {
    "list": "ArrayList/LinkedList",
    "tuple": "sem equivalente geral direto no núcleo tradicional",
    "set": "HashSet/TreeSet",
    "dict": "HashMap/TreeMap",
    "iteracao": "Iterator<E> / enhanced for",
}

if __name__ == "__main__":
    for python, java in COMPARACAO.items():
        print(f"{python:10} -> {java}")
