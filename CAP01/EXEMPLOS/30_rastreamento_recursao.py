"""Exemplo — rastrear argumentos e retornos durante recursão."""
def nossa_soma(inferior,superior,margem=0):
    espacos=' '*margem; print(espacos,inferior,superior)
    if inferior>superior:
        print(espacos,0); return 0
    resultado=inferior+nossa_soma(inferior+1,superior,margem+4)
    print(espacos,resultado); return resultado
print(nossa_soma(1,4))
