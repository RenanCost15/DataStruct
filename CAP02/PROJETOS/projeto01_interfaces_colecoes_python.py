"""Projeto 01 — Explorar as interfaces das coleções nativas do Python.

Enunciado em PT-BR:
Explore str, list, tuple, set e dict usando dir e help. A resolução abaixo
mostra os membros públicos e explica como obter a documentação completa.
"""

def explorar():
    for tipo in (str, list, tuple, set, dict):
        publicos = [nome for nome in dir(tipo) if not nome.startswith("_")]
        print(f"\n{tipo.__name__}")
        print("Métodos/atributos públicos:")
        print(", ".join(publicos))
        print("Para documentação detalhada execute: help(%s)" % tipo.__name__)

if __name__ == "__main__":
    explorar()
